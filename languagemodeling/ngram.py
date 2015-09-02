#    https://docs.python.org/3/library/collections.html
from collections import defaultdict
from math import log


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
            return float(self.count(tuple(tokens)) / self.count(tuple(prev_tokens)))
        
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
