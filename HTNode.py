# -*- coding: utf-8 -*-


from functools import total_ordering


@total_ordering
class HTNode:
    def __init__(self, char, counter):
        self.char, self.freq, self.left, self.right = char, counter, None, None

    def __lt__(self, other):

        return self.freq < other.freq

    def __eq__(self, other):
        if other is None:
            return False

        if not isinstance(other, HTNode):
            return self.freq == other.freq
