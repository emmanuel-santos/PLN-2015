# https://docs.python.org/3/library/unittest.html
from unittest import TestCase
from math import log2

from nltk.tree import Tree
from nltk.grammar import PCFG

from parsing.cky_parser import CKYParser


class TestCKYParser(TestCase):

    def test_parse(self):
        grammar = PCFG.fromstring(
            """
                S -> NP VP              [1.0]
                NP -> Det Noun          [0.6]
                NP -> Noun Adj          [0.4]
                VP -> Verb NP           [1.0]
                Det -> 'el'             [1.0]
                Noun -> 'gato'          [0.9]
                Noun -> 'pescado'       [0.1]
                Verb -> 'come'          [1.0]
                Adj -> 'crudo'          [1.0]
            """)

        parser = CKYParser(grammar)

        lp, t = parser.parse('el gato come pescado crudo'.split())

        # check chart
        pi = {
            (1, 1): {'Det': log2(1.0)},
            (2, 2): {'Noun': log2(0.9)},
            (3, 3): {'Verb': log2(1.0)},
            (4, 4): {'Noun': log2(0.1)},
            (5, 5): {'Adj': log2(1.0)},

            (1, 2): {'NP': log2(0.6 * 1.0 * 0.9)},
            (2, 3): {},
            (3, 4): {},
            (4, 5): {'NP': log2(0.4 * 0.1 * 1.0)},

            (1, 3): {},
            (2, 4): {},
            (3, 5): {'VP': log2(1.0) + log2(1.0) + log2(0.4 * 0.1 * 1.0)},

            (1, 4): {},
            (2, 5): {},

            (1, 5): {'S':
                     log2(1.0) +  # rule S -> NP VP
                     log2(0.6 * 1.0 * 0.9) +  # left part
                     log2(1.0) + log2(1.0) + log2(0.4 * 0.1 * 1.0)},  # right part
        }
        self.assertEqualPi(parser._pi, pi)

        # check partial results
        bp = {
            (1, 1): {'Det': Tree.fromstring("(Det el)")},
            (2, 2): {'Noun': Tree.fromstring("(Noun gato)")},
            (3, 3): {'Verb': Tree.fromstring("(Verb come)")},
            (4, 4): {'Noun': Tree.fromstring("(Noun pescado)")},
            (5, 5): {'Adj': Tree.fromstring("(Adj crudo)")},

            (1, 2): {'NP': Tree.fromstring("(NP (Det el) (Noun gato))")},
            (2, 3): {},
            (3, 4): {},
            (4, 5): {'NP': Tree.fromstring("(NP (Noun pescado) (Adj crudo))")},

            (1, 3): {},
            (2, 4): {},
            (3, 5): {'VP': Tree.fromstring(
                "(VP (Verb come) (NP (Noun pescado) (Adj crudo)))")},

            (1, 4): {},
            (2, 5): {},

            (1, 5): {'S': Tree.fromstring(
                """(S
                    (NP (Det el) (Noun gato))
                    (VP (Verb come) (NP (Noun pescado) (Adj crudo)))
                   )
                """)},
        }
        self.assertEqual(parser._bp, bp)

        # check tree
        t2 = Tree.fromstring(
            """
                (S
                    (NP (Det el) (Noun gato))
                    (VP (Verb come) (NP (Noun pescado) (Adj crudo)))
                )
            """)
        self.assertEqual(t, t2)

        # check log probability
        lp2 = log2(1.0 * 0.6 * 1.0 * 0.9 * 1.0 * 1.0 * 0.4 * 0.1 * 1.0)
        self.assertAlmostEqual(lp, lp2)

    def test_parse_ambiguity(self):
        grammar = PCFG.fromstring(
            """
                S -> NP VP              [1.0]
                NP -> Det Noun          [0.5]
                NP -> Noun Adj          [0.3]
                NP -> Det NP            [0.2]
                VP -> VP Adj            [0.3]
                VP -> Verb NP           [0.7]
                Det -> 'a'              [0.5]
                Det -> 'el'             [0.5]
                Noun -> 'hombre'        [0.6]
                Noun -> 'Jorge'         [0.4]
                Verb -> 'vio'           [1.0]
                Adj -> 'enfurecido'     [1.0]
            """)

        parser = CKYParser(grammar)

        lp, t = parser.parse('el hombre vio a Jorge enfurecido'.split())

        # check chart
        pi = {
            (1, 1): {'Det': log2(0.5)},
            (2, 2): {'Noun': log2(0.6)},
            (3, 3): {'Verb': log2(1.0)},
            (4, 4): {'Det': log2(0.5)},
            (5, 5): {'Noun': log2(0.4)},
            (6, 6): {'Adj': log2(1.0)},

            (1, 2): {'NP': log2(0.5 * 0.5 * 0.6)},
            (2, 3): {},
            (3, 4): {},
            (4, 5): {'NP': log2(0.5 * 0.5 * 0.4)},
            (5, 6): {'NP': log2(0.3 * 0.4 * 1.0)},

            (1, 3): {},
            (2, 4): {},
            (3, 5): {'VP': log2(0.7 * 1.0 * 0.5 * 0.5 * 0.4)},
            (4, 6): {'NP': log2(0.2 * 0.5 * 0.3 * 0.4 * 1.0)},

            (1, 4): {},
            (2, 5): {},
            (3, 6): {'VP': log2(0.3 * 0.7 * 1.0 * 0.5 * 0.5 * 0.4 * 1.0)},
            # log2(0.7 * 1.0 * 0.2 * 0.5 * 0.3 * 0.4 * 1.0) (ambiguity detected)

            (1, 5): {'S':
                     log2(1.0) +  # rule S -> NP VP
                     log2(0.5 * 0.5 * 0.6) +  # left part
                     log2(0.7 * 1.0 * 0.5 * 0.5 * 0.4)},  # right part
            (2, 6): {},


            (1, 6): {'S':
                     log2(1.0) +  # rule S -> NP VP
                     log2(0.5 * 0.5 * 0.6) +  # left part
                     log2(0.3 * 0.7 * 1.0 * 0.5 * 0.5 * 0.4 * 1.0)},  # right part
        }
        self.assertEqualPi(parser._pi, pi)

        # check partial results
        bp = {
            (1, 1): {'Det': Tree.fromstring("(Det el)")},
            (2, 2): {'Noun': Tree.fromstring("(Noun hombre)")},
            (3, 3): {'Verb': Tree.fromstring("(Verb vio)")},
            (4, 4): {'Det': Tree.fromstring("(Det a)")},
            (5, 5): {'Noun': Tree.fromstring("(Noun Jorge)")},
            (6, 6): {'Adj': Tree.fromstring("(Adj enfurecido)")},

            (1, 2): {'NP': Tree.fromstring("(NP (Det el) (Noun hombre))")},
            (2, 3): {},
            (3, 4): {},
            (4, 5): {'NP': Tree.fromstring("(NP (Det a) (Noun Jorge))")},
            (5, 6): {'NP': Tree.fromstring("(NP (Noun Jorge) (Adj enfurecido))")},

            (1, 3): {},
            (2, 4): {},
            (3, 5): {'VP': Tree.fromstring(
                "(VP (Verb vio) (NP (Det a) (Noun Jorge)))")},
            (4, 6): {'NP': Tree.fromstring(
                "(NP (Det a) (NP (Noun Jorge) (Adj enfurecido)))")},

            (1, 4): {},
            (2, 5): {},
            (3, 6): {'VP': Tree.fromstring(
                """(VP
                    (VP (Verb vio) (NP (Det a) (Noun Jorge)))
                    (Adj enfurecido)
                    )
                """)},

            (1, 5): {'S': Tree.fromstring(
                """(S
                    (NP (Det el) (Noun hombre))
                    (VP (Verb vio) (NP (Det a) (Noun Jorge)))
                   )
                """)},
            (2, 6): {},

            (1, 6): {'S': Tree.fromstring(
                """(S
                    (NP (Det el) (Noun hombre))
                    (VP
                     (VP (Verb vio) (NP (Det a) (Noun Jorge)))
                     (Adj enfurecido)
                    )
                   )
                """)},

        }
        self.assertEqualBp(parser._bp, bp)

        # check tree
        t2 = Tree.fromstring(
            """(S
                (NP (Det el) (Noun hombre))
                (VP
                 (VP (Verb vio) (NP (Det a) (Noun Jorge)))
                 (Adj enfurecido)
                )
               )
            """)
        self.assertEqual(t, t2)

        # check log probability
        lp2 = log2(1.0 * 0.5 * 0.5 * 0.6 * 0.3 * 0.7 * 1.0 * 0.5 * 0.5 * 0.4 * 1.0)
        self.assertAlmostEqual(lp, lp2)

    def assertEqualPi(self, pi1, pi2):
        self.assertEqual(set(pi1.keys()), set(pi2.keys()))

        for k in pi1.keys():
            d1, d2 = pi1[k], pi2[k]
            self.assertEqual(d1.keys(), d2.keys(), k)
            for k2 in d1.keys():
                prob1 = d1[k2]
                prob2 = d2[k2]
                self.assertAlmostEqual(prob1, prob2)

    def assertEqualBp(self, bp1, bp2):
        self.assertEqual(set(bp1.keys()), set(bp2.keys()))

        for k in bp1.keys():
            d1, d2 = bp1[k], bp2[k]
            self.assertEqual(d1.keys(), d2.keys(), k)
            for k2 in d1.keys():
                tree1 = d1[k2]
                tree2 = d2[k2]
                self.assertEqual(tree1, tree2)
