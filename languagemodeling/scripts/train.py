"""Train an n-gram model.

Usage:
  train.py -n <n> [-m <model>] [-a <addone>] -o <file>
  train.py -h | --help

Options:
  -n <n>        Order of the model.
  -m <model>    Model to use [default: ngram]:
                  ngram: Unsmoothed n-grams.
                  addone: N-grams with add-one smoothing.
                  interpolated: N-grams whit interpolated.
                  backoff: .
  -a <addone>   Use addone [default : True]
  -o <file>     Output model file.
  -h --help     Show this screen.
"""
from docopt import docopt
import pickle

from nltk.corpus import PlaintextCorpusReader
from nltk import RegexpTokenizer

pattern = r'''(?x)    # set flag to allow verbose regexps
([A-Z]\.)+        # abbreviations, e.g. U.S.A.
| \w+(-\w+)*        # words with optional internal hyphens
| \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
| \.\.\.            # ellipsis
| [][.,;"'?():-_`]
'''

tokenizer = RegexpTokenizer(pattern)
corpus = PlaintextCorpusReader('.', 'corpus/Harrypotter.txt', word_tokenizer=tokenizer)

from languagemodeling.ngram import NGram, AddOneNGram, InterpolatedNGram, BackOffNGram

if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the data
    sents = corpus.sents('corpus/Harrypotter.txt')
    sents = sents[:int(0.9*len(sents))]

    # train the model
    n = int(opts['-n'])
    m = opts['-m']
    addone = opts['-a']
    if addone == 'False':
        addone = False
    else:
        addone = True

    if m == 'addone':
        model = AddOneNGram(n, sents)
    elif m == 'interpolated':
        model = InterpolatedNGram(n, sents, addone=addone)
    elif m == 'backoff':
        model = BackOffNGram(n, sents, addone=addone)
    else:
        model = NGram(n, sents)

    # save it
    filename = opts['-o']
    f = open('corpus/' + filename, 'wb')
    pickle.dump(model, f)
    f.close()
