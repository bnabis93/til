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

    def __iter__(self):
        for match in RE_WORD.finditer(self.text):
            yield match.group()

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)
