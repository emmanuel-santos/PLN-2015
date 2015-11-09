from nltk.tree import Tree
from math import log2
from collections import defaultdict


class CKYParser:

    def __init__(self, grammar):
        """
        grammar -- a binarised NLTK PCFG.
        """
        self.grammar = grammar
        self.rproduction = rproduction = defaultdict(list)
      
        for production in grammar.productions():
            if production.is_nonlexical():
                r0 = str(production.rhs()[0])
                r1 = str(production.rhs()[1])
                rproduction[(r0, r1)] += [production]

        self._pi = {}
        self._bp = {}

    def parse(self, sent):
        """Parse a sequence of terminals.

        sent -- the sequence of terminals.
        """
        productions = self.grammar.productions()
        start = str(self.grammar.start())
        rprod = self.rproduction
        self._pi = pi = dict()
        self._bp = bp = dict()
        lp = 0
        t = None

        j = 1
        # inicializacion
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

        # cky
        for i in range(1, len(sent)):
            for j in range(1, len(sent) - (i - 1)):
                l = i + j
                bp[(j, l)] = {}
                pi[(j, l)] = {}
                for k in range(j, l):
                    for r0 in pi[(j, k)]:
                        for r1 in pi[((k + 1), l)]:
                            lp1 = pi[(j, k)][r0]
                            lp2 = pi[((k + 1), l)][r1]
                            for production in rprod[(r0, r1)]:
                                Nonterminal = str(production.lhs())
                                prob = log2(production.prob())
                                prob = prob + lp1 + lp2
                                if (Nonterminal not in pi[(j, l)] or
                                   prob > pi[(j, l)][Nonterminal]):

                                    pi[(j, l)][Nonterminal] = prob
                                    left = bp[(j, k)][r0]
                                    right = bp[((k + 1), l)][r1]
                                    tree = Tree(Nonterminal, [left, right])
                                    bp[(j, l)][Nonterminal] = tree

        # print(start)
        # print(pi[(1,len(sent))])
        if str(start) in pi[(1, len(sent))]:
            lp = pi[(1, len(sent))][start]
            t = bp[(1, len(sent))][start]

        return (lp, t)
