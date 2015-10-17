"""Evaulate a tagger.

Usage:
  eval.py -i <file>
  eval.py -h | --help

Options:
  -i <file>     Tagging model file.
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle
import sys

from corpus.ancora import SimpleAncoraCorpusReader


def progress(msg, width=None):
    """Ouput the progress of something on the same line."""
    if not width:
        width = len(msg)
    print('\b' * width + msg, end='')
    sys.stdout.flush()


if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the model
    filename = opts['-i']
    f = open(filename, 'rb')
    model = pickle.load(f)
    f.close()

    # load the data
    files = '3LB-CAST/.*\.tbf\.xml'

    corpus = SimpleAncoraCorpusReader('ancora/ancora-2.0/', files)
    sents = list(corpus.tagged_sents())

    # tag
    hits_known, total_known = 0,0
    hits_unknown, total_unknown = 0, 0
    hits, total = 0, 0
    n = len(sents)
    for i, sent in enumerate(sents):
        word_sent, gold_tag_sent = zip(*sent)

        model_tag_sent = model.tag(word_sent)
        assert len(model_tag_sent) == len(gold_tag_sent), i

        # global score
        hits_sent = [m == g for m, g in zip(model_tag_sent, gold_tag_sent)]
        hits += sum(hits_sent)
        total += len(sent)

    
        for j , tag in enumerate(model_tag_sent):
            gold_tag = gold_tag_sent[j]
            model_tag_word = tag
            
            if model.unknown(word_sent[j]):
                hit_unknown_word = model_tag_word == gold_tag    
                hits_unknown += hit_unknown_word
                total_unknown += 1
            else:
                hit_known_word = model_tag_word == gold_tag
                hits_known += hit_known_word
                total_known += 1

        progress('Progress: {:3.1f}%'.format(float(i) * 100 / n))

    acc_unknown = float(hits_unknown) / total_unknown
    acc_known = float(hits_known) / total_known 
    acc = float(hits) / total

    print('')
    print('Accuracy: {:2.2f}%'.format(acc * 100))
    print('')
    print('Accuracy Know: {:2.2f}%'.format(acc_known * 100))
    print('')
    print('Accuracy UnKnow: {:2.2f}%'.format(acc_unknown * 100))