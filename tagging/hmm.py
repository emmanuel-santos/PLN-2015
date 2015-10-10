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

        log_prob_tagging = 1.0

        L = ['<s>'] * (n - 1) + y + ['</s>']

        for i in range(len(L) - n + 1):
            t_p = self.trans_prob(L[i + n - 1], tuple(L[i: i + n - 1]))
            if t_p != 0: 
                log_prob_tagging *= log2(t_p)
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
        tagging_more_prob = []
        for word in sent:
            prob_tagging = []
            num = []
            for tag in self.tagset():
                prob_tagging += [(tag, self.out_prob(word, tag))]
            tagging_more_prob += [max(prob_tagging, key=itemgetter(1))[0]]    
        return tagging_more_prob
 


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
        lenght = len(sent) 
        self._pi = defaultdict(dict)
        
        starts = ['<s>'] * (n - 1)
        self._pi[0][tuple(starts)] = (0, [])

        for i in range(lenght):
            for tag in hmm.tags:
                prob = float("-inf")
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
        for elem in self._pi[lenght]:
            logs_p_tagging += [tuple(self._pi[lenght][elem])]
            
        sequence = max(logs_p_tagging, key=itemgetter(0))[1]

        return sequence
