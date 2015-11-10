from nltk.grammar import Nonterminal
from nltk.tree import Tree
from nltk import induce_pcfg
from .util import unlexicalize, lexicalize
from .cky_parser import CKYParser


class UPCFG:
    """Unlexicalized PCFG.
    """

    def __init__(self, parsed_sents, start='sentence', horzMarkov=None):
        """
        parsed_sents -- list of training trees.
        """
        self.start = start

        prod = []
        for t in parsed_sents:
            t1 = t.copy(deep=True)
            t1 = unlexicalize(t1)
            t1.chomsky_normal_form(horzMarkov=horzMarkov)
            t1.collapse_unary(collapsePOS=True, collapseRoot=True)
            prod += t1.productions()
        grammar = induce_pcfg(Nonterminal(start), prod)
        self.product = grammar.productions()
        self.cky_parser = CKYParser(grammar)

    def productions(self):
        """Returns the list of UPCFG probabilistic productions.
        """
        return self.product

    def parse(self, tagged_sent):
        """Parse a tagged sentence.

        tagged_sent -- the tagged sentence (a list of pairs (word, tag)).
        """
        sent, tags = zip(*tagged_sent)
        lp, t = self.cky_parser.parse(tags)
        if t is None:
            t = Tree(self.start, [Tree(tag, [word]) for word, tag in tagged_sent])
            return t
        t.un_chomsky_normal_form()
        t = lexicalize(t, sent)
        return t
