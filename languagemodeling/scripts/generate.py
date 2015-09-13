"""Generate natural language sentences using a language model.

Usage:
  generate.py -i <file> -n <n>
  generate.py -h | --help

Options:
  -i <file>     Language model file.
  -n <n>        Number of sentences to generate.
  -h --help     Show this screen."""

from docopt import docopt
import pickle
import pdb


from languagemodeling.ngram import NGramGenerator


if __name__ == '__main__':
    opts = docopt(__doc__)

    # read options
    n = int(opts['-n'])
    filename = opts['-i']
    
 
    f = open('corpus/' + filename, 'rb')
    model = pickle.load(f)
    f.close()
    generator = NGramGenerator(model)

    # create new_sents
    for i in range(n):
     new_sent = generator.generate_sent()
     print(' '.join(new_sent))
