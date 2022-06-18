from abc import abstractmethod
from typing import Iterable


class Iterator(Iterable):
    """Iterator example."""

    __slots__ = ()

    @abstractmethod
    def __next__(self):
        """Abstract method. 상속받는 친구들은 이부분이 구현되어있어야 한다."""
        raise StopIteration

    def __iter__(self):
        return self

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Iterator:
            if any("__next__" in B.__dict__ for B in C.__mro__) and any(
                "__iter__" in B.__dict__ for B in C.__mro__
            ):
                return True
        return NotImplemented
