#    https://docs.python.org/3/library/collections.html
from collections import defaultdict
from math import log
import random
import pdb


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


    def Log_probability(self, sents):
        """
        sents -- list of sentences, each one being a list of tokens.
        """    
        log_probability = 0.0
        for sent in sents:
            log_probability += self.sent_log_prob(sent)

        return  log_probability


    def cross_entropy(self, sents):
        """
        sents -- list of sentences, each one being a list of tokens.
        """
        M = 0
        for sent in sents:
            M += len(sent) + 1 
        
        return (-1/M) * self.Log_probability(sents)


    def perplexity(self, sents):
        """
        sents -- list of sentences, each one being a list of tokens.
        """
        cross_entropy = self.cross_entropy(sents)

        return 2 ** cross_entropy


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

        for c,l in self.probs.items():
            self.sorted_probs[c] = sorted(l.items(), key =lambda asd: (-asd[1], asd[0]))

 
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

        prob = 0.0
        
        for i in possibles_tokens:
            prob += i[1] 
            if r <= prob:
                return i[0]
        
        assert False

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
            if new_token == '</s>': 
                ubicacion = len(sent) - 1 # agarramos la ultima ubicacion 
                del sent[ubicacion] 
                break
            prev_tokens += [new_token]     
            prev_tokens = prev_tokens[1:]

        return sent


class AddOneNGram(NGram):

    def __init__(self, n, sents):

        NGram.__init__(self, n, sents)

        alphabet = []

        for l,c in self.counts.items():
            if len(l) == self.n:
                for i in l:
                    alphabet += [i]
        alphabet = list(set(alphabet))
        if '<s>' in alphabet:
            del alphabet[alphabet.index('<s>')]
        
        self.v = len(alphabet)


    def V(self):
        """Size of the vocabulary."""
        return self.v

   
    def cond_prob(self, token, prev_tokens=None):
        """Conditional probability of a token.
        token -- the token.
        prev_tokens -- the previous n-1 tokens (optional only if n = 1).
        """
        n = self.n
        if not prev_tokens:
            prev_tokens = []
        assert len(prev_tokens) == n - 1

        tokens = prev_tokens + [token]

        return (self.count(tuple(tokens)) + 1.0) / (float(self.count(tuple(prev_tokens)) + self.V()))



class InterpolatedNGram(NGram):
 
    def __init__(self, n, sents, gamma=None, addone=True):
        """
        n -- order of the model.
        sents -- list of sentences, each one being a list of tokens.
        gamma -- interpolation hyper-parameter (if not given, estimate using
            held-out data).
        addone -- whether to use addone smoothing (default: True).
        """
        NGram.__init__(self, n, sents)
        
        self.gamma = gamma
        held_out = sents[int(0.9*len(sents)):]
        sents = sents[:int(0.9*len(sents))]

        self.addone = addone

