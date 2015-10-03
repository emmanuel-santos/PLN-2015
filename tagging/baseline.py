from collections import defaultdict

class BaselineTagger:

    def __init__(self, tagged_sents):
        """
        tagged_sents -- training sentences, each one being a list of pairs.
        """
        self.tagged = tagged = defaultdict(int)
        self.t_w = t_w = defaultdict(str)

        for sent in tagged_sents:
            for word, tag in sent:
                tagged[tag] += 1
                t_w[word] = tag

        tagged = sorted(tagged.items(), key=lambda tag_w: -tag_w[1])
        
        self.tag_more_common = tagged[0][0] 


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
