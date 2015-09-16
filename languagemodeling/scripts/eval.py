"""
$ python languagemodeling/scripts/eval.py  --help
Evaulate a language model using the test set.

Usage:
  eval.py -i <file>
  eval.py -h | --help

Options:
  -i <file>     Language model file.
  -h --help     Show this screen.
"""
from docopt import docopt

from languagemodeling.ngram import NGram, AddOneNGram
import pickle

from nltk.corpus import PlaintextCorpusReader
from nltk import RegexpTokenizer

pattern = r'''(?x)    # set flag to allow verbose regexps
([A-Z]\.)+        	# abbreviations, e.g. U.S.A.
| \w+(-\w+)*        # words with optional internal hyphens
| \$?\d+(\.\d+)?%?  # currency and percentages, e.g. $12.40, 82%
| \.\.\.            # ellipsis
| [][.,;"'?():-_`]  #  
'''

tokenizer = RegexpTokenizer(pattern)
corpus = PlaintextCorpusReader('.', 'corpus/Harrypotter.txt', word_tokenizer = tokenizer)

if __name__ == '__main__':
    opts = docopt(__doc__)

    i = opts['-i']

    file = open('corpus/' + i, 'rb')
    model = pickle.load(file)
    file.close()

    # load the data
    sents = corpus.sents('corpus/Harrypotter.txt')

    # separate corpus
    sents = sents[int(0.9*len(sents)):]

    # estimate perplexity
    perplexity = model.perplexity(sents)

    print(perplexity)
