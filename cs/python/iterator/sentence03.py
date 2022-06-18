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
        for word in self.words:
            yield word

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)
