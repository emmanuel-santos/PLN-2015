from collections import defaultdict
from math import log2
from operator import itemgetter

class HMM:
 
    def __init__(self, n, tagset, trans, out):
        """
        n -- n-gram size.
        tagset -- set of tags.
        trans -- transition probabilities dictionary.
        out -- output probabilities dictionary.
        """
        self.n = n
        self.tags = tagset
        self.trans = trans
        self.out = out

 
    def tagset(self):
        """Returns the set of tags.
        """
        return self.tags
 

    def trans_prob(self, tag, prev_tags):
        """Probability of a tag.
 
        tag -- the tag.
        prev_tags -- tuple with the previous n-1 tags (optional only if n = 1).
        """
        n = self.n
        trans = self.trans
        trans_p = 0.0

        if not prev_tags:
            prev_tags = []
        
        assert len(prev_tags) == n - 1

        if (prev_tags in trans) and (tag in trans[prev_tags]): 
            trans_p = trans[prev_tags][tag]

        return trans_p

 
    def out_prob(self, word, tag):
        """Probability of a word given a tag.
 
        word -- the word.
        tag -- the tag.
        """
        out = self.out
        out_p = 0.0 

        if (tag in out) and (word in out[tag]): 
            out_p = out[tag][word]

        return out_p
 

    def tag_prob(self, y):
        """
        Probability of a tagging.
        Warning: subject to underflow problems.
 
        y -- tagging.
        """
        n = self.n

        prob_tagging = 1.0

        L = ['<s>'] * (n - 1) + y + ['</s>']

        for i in range(len(L) - n + 1):
            prob_tagging *= self.trans_prob(L[i + n - 1], 
                                            tuple(L[i: i + n - 1]))

        return float(prob_tagging)


    def prob(self, x, y):
        """
        Joint probability of a sentence and its tagging.
        Warning: subject to underflow problems.
 
        x -- sentence.
        y -- tagging.
        """
        prob = 1.0

        for i,tag in enumerate(y):
            prob *= self.out_prob(x[i], tag)

        return prob * self.tag_prob(y)  


    def tag_log_prob(self, y):
        """
        Log-probability of a tagging.
 
        y -- tagging.
        """
        n = self.n

        t_p = 1.0

        L = ['<s>'] * (n - 1) + y + ['</s>']

        for i in range(len(L) - n + 1):
            t_p *= self.trans_prob(L[i + n - 1], tuple(L[i: i + n - 1]))

        if t_p != 0: 
            log_prob_tagging = log2(t_p)
        else: 
            return float("-inf")

        return log_prob_tagging
 

    def log_prob(self, x, y):
        """
        Joint log-probability of a sentence and its tagging.
 
        x -- sentence.
        y -- tagging.
        """
        log_p = float('-inf')
        if self.prob(x, y) != 0:
            log_p = log2(self.prob(x, y))

        return log_p 
 

    def tag(self, sent):
        """Returns the most probable tagging for a sentence.
 
        sent -- the sentence.
        """
        viterbi = ViterbiTagger(self)

        return viterbi.tag(sent)

 


class ViterbiTagger:
 
    def __init__(self, hmm):
        """
        hmm -- the HMM.
        """
        self.hmm = hmm
 
    def tag(self, sent):
        """Returns the most probable tagging for a sentence.
 
        sent -- the sentence.
        """
        hmm = self.hmm
        n = hmm.n
        length = len(sent) 
        self._pi = defaultdict(dict)
        
        starts = ['<s>'] * (n - 1)
        self._pi[0][tuple(starts)] = (0, [])

        for i in range(length):
            prob = float("-inf")
            for tag in hmm.tags:
                for prev_tags, (log_prob, tags) in self._pi[i].items():
                    t_p = hmm.trans_prob(tag, prev_tags)
                    o_p = hmm.out_prob(sent[i], tag)
                    if t_p != 0:
                        log_t_p = log2(t_p)
                    else:
                        log_t_p = float("-inf")
                    if o_p != 0:
                        log_o_p = log2(o_p)
                    else:
                        log_o_p = float("-inf")
                    
                    if prob < log_prob + log_o_p + log_t_p:
                        prob = log_prob + log_o_p + log_t_p
                        prev_t = tuple(list(prev_tags[1:]) + [tag])
                        log_p_tagging = (prob, self._pi[i][prev_tags][1] + [tag])
                        self._pi[i + 1][prev_t] = log_p_tagging

        logs_p_tagging = []
        for elem in self._pi[length]:
            logs_p_tagging += [tuple(self._pi[length][elem])]
            
        sequence = max(logs_p_tagging, key=itemgetter(0))[1]

        return sequence




class MLHMM(HMM):
 
    def __init__(self, n, tagged_sents, addone=True):
        """
        n -- order of the model.
        tagged_sents -- training sentences, each one being a list of pairs.
        addone -- whether to use addone smoothing (default: True).
        """
        self.addone = addone
        self.n = n
        self.tags = set()
        
        self.tagged_c = tagged_c = defaultdict(int)
        self.tagged_word = tagged_word = defaultdict(int)

        for sent in tagged_sents:
            words, tags = zip(*sent)
            L = ['<s>'] * (n - 1) + list(tags) + ['</s>']
            for i in range(len(L) - n + 1):
                ngram = tuple(L[i: i + n])
                tagged_c[ngram] += 1
                tagged_c[ngram[:-1]] += 1
            for word, tag in sent:
                tagged_word[(word, tag)] += 1 
                self.tags.add(tag)

 
    def tcount(self, tokens):
        """Count for an k-gram for k <= n.
 
        tokens -- the k-gram tuple.
        """
        return self.tagged_c[tokens]
 
    def unknown(self, w):
        """Check if a word is unknown for the model.
 
        w -- the word.
        """
        return (not w in [item[0] for item in self.tagged_word if item[0] == w])
 
    def tagset(self):
        """Returns the set of tags.
        """
        return self.tags

    def trans_prob(self, tag, prev_tags):
        """Probability of a tag.
 
        tag -- the tag.
        prev_tags -- tuple with the previous n-1 tags (optional only if n = 1).
        """
        if self.addone:
            return ((self.tagged_c[prev_tags + (tag,)] + 1) /
                    (self.tagged_c[prev_tags] + len(self.tags)))

        if prev_tags + (tag,) not in self.tagged_c:
            return 0

        return (self.tagged_c[prev_tags + (tag,)] /
            self.tagged_c[prev_tags])

    def out_prob(self, word, tag):
        """Probability of a word given a tag.

        word -- the word.
        tag -- the tag.
        """
        if self.unknown(word):
            return 0.0

        total = 0.0
        for item in self.tagged_word:
            if item[1] == tag:
                total += self.tagged_word[item]

        return (self.tagged_word[(word, tag)] / total)        

    def tag_prob(self, y):
        """
        Probability of a tagging.
        Warning: subject to underflow problems.
 
        y -- tagging.
        """
        n = self.n

        prob_tagging = 1.0

        L = ['<s>'] * (n - 1) + y + ['</s>']

        for i in range(len(L) - n + 1):
            prob_tagging *= self.trans_prob(L[i + n - 1], 
                                            tuple(L[i: i + n - 1]))

        return prob_tagging

    def prob(self, x, y):
        """
        Joint probability of a sentence and its tagging.
        Warning: subject to underflow problems.
 
        x -- sentence.
        y -- tagging.
        """
        prob = 1.0

        for i,tag in enumerate(y):
            prob *= self.out_prob(x[i], tag)

        return prob * self.tag_prob(y)  


    def tag_log_prob(self, y):
        """
        Log-probability of a tagging.
 
        y -- tagging.
        """
        n = self.n

        t_p = 1.0

        L = ['<s>'] * (n - 1) + y + ['</s>']

        for i in range(len(L) - n + 1):
            t_p *= self.trans_prob(L[i + n - 1], tuple(L[i: i + n - 1]))

        if t_p != 0: 
            log_prob_tagging = log2(t_p)
        else: 
            return float("-inf")

        return log_prob_tagging
 

    def log_prob(self, x, y):
        """
        Joint log-probability of a sentence and its tagging.
 
        x -- sentence.
        y -- tagging.
        """
        log_p = float('-inf')
        if self.prob(x, y) != 0:
            log_p = log2(self.prob(x, y))

        return log_p 
 

    def tag(self, sent):
        """Returns the most probable tagging for a sentence.
 
        sent -- the sentence.
        """
        viterbi = ViterbiTagger(self)

        return viterbi.tag(sent)
        


