#    https://docs.python.org/3/library/collections.html
from collections import defaultdict
from math import log
import random


class NGram(object):

    def __init__(self, n, sents):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        """
        assert n > 0
        self.n = n
        self.counts = counts = defaultdict(int)

        for sent in sents:
            L = []
            for i in range(n - 1):
                L += ['<s>'] 
            L += sent + ['</s>']
            for i in range(len(L) - n + 1):
                ngram = tuple(L[i: i + n])
                counts[ngram] += 1
                counts[ngram[:-1]] += 1


    def count(self, tokens):
        """Count for an n-gram or (n-1)-gram.
 
        tokens -- the n-gram or (n-1)-gram tuple.
        """

        return self.counts[tokens]  


    def cond_prob(self, token, prev_tokens=None):
        n = self.n
        if not prev_tokens:
            prev_tokens = []
        
        assert len(prev_tokens) == n - 1

        tokens = prev_tokens + [token]
        
        if self.count(tuple(prev_tokens)) != 0:
            return float(self.count(tuple(tokens)) / 
                            self.count(tuple(prev_tokens)))
        
        else:
            return float(self.count(tuple(tokens)) / float("inf"))
 
    def sent_prob(self, sent):
        """Probability of a sentence. Warning: subject to underflow problems.
 
        sent -- the sentence as a list of tokens.
        """
        n = self.n
        P = 1

        L = []
        for i in range(n - 1):
            L += ['<s>'] 
        L += sent + ['</s>']
        for i in range(len(L) - n + 1):
            P = P * self.cond_prob(L[i + n - 1] , L[i: i + n - 1])

        return P
 
 
    def sent_log_prob(self, sent):
        """Log-probability of a sentence.
 
        sent -- the sentence as a list of tokens.
        """
        n = self.n
        P = 0
        log2 = lambda x: log(x, 2)
        
        L = []
        for i in range(n - 1):
            L += ['<s>'] 
        L += sent + ['</s>']
        for i in range(len(L) - n + 1):
            if self.cond_prob(L[i + n - 1] , L[i: i + n - 1]) != 0:
                P += log2(self.cond_prob(L[i + n - 1] , L[i: i + n - 1]))
            else:
                P = float("-inf")
                return P
        
        return P 


class NGramGenerator:
 
    def __init__(self, model):
        """
        model -- n-gram model.
        """
        self.probs = probs = defaultdict(dict)
        self.sorted_probs = sorted_probs = defaultdict(list)
        self.n = n = model.n
        self.counts = counts = model.counts
        
        for c,l in counts.items():
            if len(c) == n: 
                probs[c[:-1]][c[-1:][0]] = model.cond_prob(c[-1:][0],
                                                            list(c[:-1]))           
                
                sorted_probs[c[:-1]].append((c[-1:][0] , model.cond_prob(c[-1:][0],
                                                                        list(c[:-1]))))
                sorted_probs[c[:-1]].sort()

 
    def generate_token(self, prev_tokens=None):
        """Randomly generate a token, given prev_tokens.
 
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """      
        n = self.n
        if not prev_tokens:
            prev_tokens = ()
        
        assert len(prev_tokens) == n - 1

        r = random.random()

        possibles_tokens = self.sorted_probs[prev_tokens]

        a = 0
        b = 0
        for i in possibles_tokens:
            b += i[1] 
            if r >= a and r <= b:
                    return i[0]
            a += i[1]
    

    def generate_sent(self):
        """Randomly generate a sentence."""

        n = self.n
        sent = []

        prev_tokens = []
        for i in range(n -1):
            prev_tokens += ['<s>']

        while 1: 
            new_token = self.generate_token(tuple(prev_tokens))
            sent += [new_token]
            if tuple(sent)[-1:][0] == '</s>': 
                ubicacion = len(sent) - 1 # agarramos la ultima ubicacion 
                del sent[ubicacion] 
                break
            if n != 1:  # if n = 1, prev_tokens not change.
                prev_tokens = prev_tokens[1:]
                prev_tokens += [new_token]     

        return sent
