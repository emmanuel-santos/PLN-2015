from collections import defaultdict
from operator import itemgetter


class BaselineTagger:

    def __init__(self, tagged_sents):
        """
        tagged_sents -- training sentences, each one being a list of pairs.
        """
        self.ocurrence_tag = ocurrence_tag = defaultdict(int)
        self.word_t = word_t = defaultdict(dict)
        self.t_w = t_w = defaultdict(str)

        for sent in tagged_sents:
            for word, tag in sent:
                ocurrence_tag[tag] += 1
                try:
                    word_t[word][tag] += 1
                except:
                    word_t[word][tag] = 1

        for word, tag in word_t.items():
            t_w[word] = max(tag.items(), key=itemgetter(1))[0] 

        tag_more_common = max(ocurrence_tag.items(), key=itemgetter(1))[0]

        self.tag_more_common = tag_more_common

        
    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        return [self.tag_word(w) for w in sent]


    def tag_word(self, w):
        """Tag a word.

        w -- the word.
        """
        if not self.unknown(w):
            return self.t_w[w]
        else:
            return self.tag_more_common 
    

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        return (w not in self.t_w)
