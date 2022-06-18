"""
Sequence protocol example.

Author : qhsh9713@gmail.com
"""
import re
import reprlib

RE_WORD = re.compile("\w+")


class Sentence:
    """Sentence class for sequence protocol example."""

    def __init__(self, text: str) -> None:
        self.text = text
        self.words = RE_WORD.findall(text)
        print("Init the sentence : ", self.words)

    def __iter__(self):
        return SentenceIterator(self.words)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)


# Iterator니까 __next__, __iter__ 구현되어야 한다.
class SentenceIterator:
    """Sentence Iterator example."""

    def __init__(self, words) -> None:
        self.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word

    def __iter__(self):
        return self
