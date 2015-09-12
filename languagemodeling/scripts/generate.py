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

# class defaultlist(list): # create a new list
#     def __init__(self, fx):
#         self._fx = fx
#     def __setitem__(self, index, value):
#         while len(self) <= index:
#             self.append(self._fx())
#         list.__setitem__(self, index, value)

if __name__ == '__main__':
    opts = docopt(__doc__)

    # read options
    n = int(opts['-n'])
    filename = opts['-i']
    
 
    f = open(filename, 'rb')
    model = pickle.load(f)
    f.close()
    generator = NGramGenerator(model)

    # create new_sent
    for i in range(n):
     new_sent = generator.generate_sent()
     print(' '.join(new_sent))
