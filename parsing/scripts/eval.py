"""Evaulate a parser.

Usage:
  eval.py -i <file> [-m <m>] [-n <n>]
  eval.py -h | --help

Options:
  -i <file>     Parsing model file.
  -m <m>        Only long sentences less than or equal to m.
  -n <n>        Only the first n sentences.
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle
import sys

from corpus.ancora import SimpleAncoraCorpusReader

from parsing.util import spans


def progress(msg, width=None):
    """Ouput the progress of something on the same line."""
    if not width:
        width = len(msg)
    print('\b' * width + msg, end='')
    sys.stdout.flush()


if __name__ == '__main__':
    opts = docopt(__doc__)

    print('Loading model...')
    filename = opts['-i']
    f = open(filename, 'rb')
    model = pickle.load(f)
    f.close()

    n = opts['-n']
    m = opts['-m']
    if n is not None:
        n = int(n)
    if m is not None:
        m = int(m)

    print('Loading corpus...')
    files = '3LB-CAST/.*\.tbf\.xml'
    corpus = SimpleAncoraCorpusReader('ancora/ancora-2.0/', files)
    parsed_sents = list(corpus.parsed_sents())

    print('Parsing...')
    hits, total_gold, total_model = 0, 0, 0
    u_hits, u_total_gold, u_total_model = 0, 0, 0
    if n is None:
        n = len(parsed_sents)
    format_str = ('{:3.1f}% ({}/{})Label:(P={:2.2f}%, R={:2.2f}%, F1={:2.2f}%)'
                  ' UnLabel:(P={:2.2f}%, R={:2.2f}%, F1={:2.2f}%)')
    progress(format_str.format(0.0, 0, n, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0))
    for i, gold_parsed_sent in enumerate(parsed_sents[:n]):
        tagged_sent = gold_parsed_sent.pos()
        if m is None or len(tagged_sent) <= m:

            # parse
            model_parsed_sent = model.parse(tagged_sent)

            # compute labeled scores
            gold_spans = spans(gold_parsed_sent, unary=False)
            model_spans = spans(model_parsed_sent, unary=False)
            hits += len(gold_spans & model_spans)
            total_gold += len(gold_spans)
            total_model += len(model_spans)

            # compute labeled partial results
            prec = float(hits) / total_model * 100
            rec = float(hits) / total_gold * 100
            f1 = 2 * prec * rec / (prec + rec)

            # compute unlabeled scores
            s, x, y = zip(*gold_spans)
            u_gold_spans = set(zip(x, y))
            s, x, y = zip(*model_spans)
            u_model_spans = set(zip(x, y))
            u_hits += len(u_gold_spans & u_model_spans)
            u_total_gold += len(u_gold_spans)
            u_total_model += len(u_model_spans)

            # compute unlabeled partial results
            u_prec = float(u_hits) / u_total_model * 100
            u_rec = float(u_hits) / u_total_gold * 100
            u_f1 = 2 * u_prec * u_rec / (u_prec + u_rec)

            progress(format_str.format(float(i+1) * 100 / n, i+1, n, prec,
                                       rec, f1, u_prec, u_rec, u_f1))

    print('')
    print('Parsed {} sentences'.format(n))

    print('          | Precision | Recall | F1')
    print('---------------------------------------')
    print('Labeled   |', end='')
    print('{:2.2f}%     |'.format(prec), end='')
    print('{:2.2f}%  |'.format(rec), end='')
    print('{:2.2f}% '.format(f1))
    print('UnLabeled |', end='')
    print('{:2.2f}%     |'.format(u_prec), end='')
    print('{:2.2f}%  |'.format(u_rec), end='')
    print('{:2.2f}% '.format(u_f1))
