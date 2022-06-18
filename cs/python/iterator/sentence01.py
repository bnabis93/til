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

    def __getitem__(self, idx):
        return self.words[idx]

    def __len__(self):
        return len(self.words)

    def __repr__(self) -> str:
        # By default, reprlib.repr limits the string size to 30.
        return "Sentence(%s)" % reprlib.repr(self.text)


s = Sentence('"The time has come," the Walrus said,')
print(s)

for word in s:
    print(word)

# Indexing. This is sequence.
print(s[0])


class Foo:
    """Iterable example."""

    def __init__(self) -> None:
        pass

    def __iter__(sefl):
        pass


from collections import abc

print(issubclass(Foo, abc.Iterable))
# Sentence class is not iterable
print(issubclass(Sentence, abc.Iterable))
