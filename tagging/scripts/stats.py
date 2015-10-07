"""Print corpus statistics.

Usage:
  stats.py
  stats.py -h | --help

Options:
  -h --help     Show this screen.
"""
from docopt import docopt

from corpus.ancora import SimpleAncoraCorpusReader, AncoraCorpusReader

from collections import defaultdict

if __name__ == '__main__':
    opts = docopt(__doc__)

    # load the data
    # c = AncoraCorpusReader('ancora/ancora-2.0')
    # a, b = zip(*c.tagged_words())
    # voc = len(set(b))
    # print('voc_tag: {}'.format(voc))
    corpus = SimpleAncoraCorpusReader('ancora/ancora-2.0/')
    sents = list(corpus.tagged_sents())
    tagged_words = corpus.tagged_words()
    
    words, taggeds = zip(*tagged_words)

    ocurrence_words = len(words)
    voc_words = len(set(words))
    voc_taggeds = len(set(taggeds))
    most_repeat = []

    ocurrence_taggeds = defaultdict(int) 
    words_for_tag  = defaultdict(int) 
    for word, tagged in tagged_words:
        ocurrence_taggeds[tagged] += 1
        words_for_tag[(tagged, word)] += 1 

    ocurrence_taggeds = sorted(ocurrence_taggeds.items(), key=lambda o_tag: 
                                -o_tag[1])
    words_for_tag = sorted(words_for_tag.items(), key=lambda w_tag: -w_tag[1])
    
    # compute the statistics
    print('sents: {}'.format(len(sents)))
    print('ocurrence_words: {}'.format(ocurrence_words))
    print('vocabulary_of_words: {}'.format(voc_words))
    print('vocabulary_of_taggeds: {}'.format(voc_taggeds))

    print('\n\ntagged   ocurrence_tagged    percentage   five_words\n')
    for x in range(10):
        tag = ocurrence_taggeds[x][0]
        o_tag = ocurrence_taggeds[x][1]
        percentage = 100 * (ocurrence_taggeds[x][1] / ocurrence_words)
        words_tag = []
        for i in range(len(words_for_tag)):
            if words_for_tag[i][0][0] == tag:
                words_tag += [words_for_tag[i][0][1]]
            if len(words_tag) == 5:
                break
        print('{0:6}   {1:16d}   {2:10f}%   {3}'.format(tag, o_tag, percentage,
                                                        words_tag))
