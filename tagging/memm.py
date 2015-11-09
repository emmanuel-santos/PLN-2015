from featureforge.vectorizer import Vectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline
from collections import defaultdict
from tagging.features import *


class MEMM:

    def __init__(self, n, tagged_sents, clf='LR'):
        """
        n -- order of the model.
        tagged_sents -- list of sentences, each one being a list of pairs.
        """
        self.n = n
        self.voc = voc = set()
        self.ocurrence_tag = ocurrence_tag = defaultdict(int)

        for tagged_sent in tagged_sents:
            if tagged_sent != []:
                for word, tag in tagged_sent:
                    voc.add(word)
                    ocurrence_tag[tag] += 1

        features = (word_lower, word_istitle, word_isupper, word_isdigit)
        for i in features:
            features += (PrevWord(i),)
        for i in range(1, n):
            features += (NPrevTags(i),)
        vec = Vectorizer(features)

        if clf == 'MB':
            _clf = MultinomialNB()
        elif clf == 'SVC':
            _clf = LinearSVC()
        else:
            _clf = LogisticRegression()

        self.pipe = Pipeline([('vect', vec),
                             ('clf', _clf),
                              ])

        self.pipe.fit(self.sents_histories(tagged_sents),
                      self.sents_tags(tagged_sents))

    def sents_histories(self, tagged_sents):
        """
        Iterator over the histories of a corpus.

        tagged_sents -- the corpus (a list of sentences)
        """
        output = []
        for tagged_sent in tagged_sents:
            if tagged_sent != []:
                output += self.sent_histories(tagged_sent)

        return output

    def sent_histories(self, tagged_sent):
        """
        Iterator over the histories of a tagged sentence.

        tagged_sent -- the tagged sentence (a list of pairs (word, tag)).
        """
        n = self.n
        star = ('<s>',) * (n - 1)
        sent, tags = zip(*tagged_sent)
        sent_tags = star + tags
        output = []

        for i in range(len(sent)):
            prev_tags = sent_tags[i:i + (n - 1)]
            history = History(list(sent), prev_tags, i)
            output += [history]

        return output

    def sents_tags(self, tagged_sents):
        """
        Iterator over the tags of a corpus.

        tagged_sents -- the corpus (a list of sentences)
        """
        output = []
        for tagged_sent in tagged_sents:
            if tagged_sent != []:
                output += self.sent_tags(tagged_sent)

        return output

    def sent_tags(self, tagged_sent):
        """
        Iterator over the tags of a tagged sentence.

        tagged_sent -- the tagged sentence (a list of pairs (word, tag)).
        """
        sent, tags = zip(*tagged_sent)
        return tags

    def tag(self, sent):
        """Tag a sentence.

        sent -- the sentence.
        """
        n = self.n
        prev_tags = ('<s>',) * (n - 1)
        tagged = []

        for i in range(len(sent)):
            history = History(sent, prev_tags, i)
            tag = self.tag_history(history)[0]
            prev_tags = prev_tags + (tag,)
            prev_tags = prev_tags[1:]
            tagged += [tag]

        return tagged

    def tag_history(self, h):
        """Tag a history.

        h -- the history.
        """
        return self.pipe.predict([h])

    def unknown(self, w):
        """Check if a word is unknown for the model.

        w -- the word.
        """
        return not (w in self.voc)
