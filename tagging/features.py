from collections import namedtuple

from featureforge.feature import Feature


# sent -- the whole sentence.
# prev_tags -- a tuple with the n previous tags.
# i -- the position to be tagged.
History = namedtuple('History', 'sent prev_tags i')


def word_lower(h):
    """Feature: Current lowercased word.

    h -- a history.
    """
    sent, i = h.sent, h.i
    return sent[i].lower()


def word_istitle(h):
    """Feature: Current word begins in uppercase.

    h -- a history.
    """
    sent, i = h.sent, h.i
    return sent[i].istitle()


def word_isupper(h):
    """Feature: Current word is capitalized.

    h -- a history.
    """
    sent, i = h.sent, h.i
    return sent[i].isupper()


def word_isdigit(h):
    """Feature: Current word is a number.

    h -- a history.
    """
    sent, i = h.sent, h.i
    return sent[i].isdigit()


def prev_tags(h):
    """Feature: Previous tags.

    h -- a history.
    """
    return h.prev_tags


class NPrevTags(Feature):
 
    def __init__(self, n):
        """Feature: n previous tags tuple.
 
        n -- number of previous tags to consider.
        """
        self.n = n
 
    def _evaluate(self, h):
        """n previous tags tuple.
 
        h -- a history.
        """
        n = self.n
        all_prev_tags = prev_tags(h)
        return all_prev_tags[-n:]


 
 
class PrevWord(Feature):
 
    def __init__(self, f):
        """Feature: the feature f applied to the previous word.
 
        f -- the feature.
        """
        self.feature = f
 
    def _evaluate(self, h):
        """Apply the feature to the previous word in the history.
 
        h -- the history.
        """
        feature = self.feature
        sent, prev_tags, i = h.sent, h.prev_tags, h.i
        f_prev_word = ''
        
        if i > 0:
            prev_word = History(sent, prev_tags, (i - 1))
            f_prev_word = str(feature(prev_word))
        else:
            f_prev_word = 'BOS'

        return f_prev_word