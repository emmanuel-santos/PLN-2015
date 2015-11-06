from nltk.tree import Tree
from math import log2


class CKYParser:

    def __init__(self, grammar):
        """
        grammar -- a binarised NLTK PCFG.
        """
        self.grammar = grammar
        self.s = str(grammar.start())
        self._pi = {}
        self._bp = {}

    def parse(self, sent):
        """Parse a sequence of terminals.

        sent -- the sequence of terminals.
        """
        productions = self.grammar.productions()
        s = self.s
        self._pi = pi = dict()
        self._bp = bp = dict()

        j = 1
        for word in sent:
            for production in productions:
                leaves = production.rhs()
                if leaves[0] == word:
                    pi[(j, j)] = {}
                    bp[(j, j)] = {}
                    Nonterminal = str(production.lhs())
                    pi[(j, j)][Nonterminal] = log2(production.prob())
                    bp[(j, j)][Nonterminal] = Tree(Nonterminal, [word])
                    j += 1

        for i in range(1, len(sent)):
            for j in range(1, len(sent) - (i - 1)):
                bp[j, (i + j)] = {}
                pi[j, (i + j)] = {}
                for k in range(j, (i + j)):
                    for production in productions:
                        leaves = production.rhs()
                        if not production.is_lexical():
                            l = str(leaves[0])
                            r = str(leaves[1])
                            _from = pi[(j, k)]
                            _to = pi[((k + 1), (i + j))]
                            if l in _from and r in _to:
                                Nonterminal = str(production.lhs())
                                prob = log2(production.prob())
                                lp1 = _from[l]
                                lp2 = _to[r]
                                prob = prob + lp1 + lp2
                                if (pi[j, (i + j)] == {} or
                                   prob > pi[j, (i + j)][Nonterminal]):

                                    pi[j, (i + j)][Nonterminal] = prob
                                    left = bp[(j, k)][l]
                                    right = bp[((k + 1), (i + j))][r]
                                    tree = Tree(Nonterminal, [left, right])
                                    bp[j, (i + j)][Nonterminal] = tree

        lp = pi[(1, len(sent))][s]
        t = bp[(1, len(sent))][s]
        return (lp, t)
