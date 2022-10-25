# class Solution:
#     def isSubsequence(self, s: str, t: str) -> bool:


from itertools import product
from tkinter.tix import Tree

"""
s가 t의 subsequence가 될 수 있는가?
- subsequence는 상대적인 위치를 변하게 하지않고, 일부 string을 지워 해당 string을 만들 수 있으면 subsequence라 함


"""


def is_subsequence(s: str, t: str) -> bool:
    """."""
    sol_len = len(s)
    char_cnt = 0

    if sol_len == 0:
        return True

    for idx, char in enumerate(t):
        target_char = s[char_cnt]

        if target_char == char:
            char_cnt += 1
        if char_cnt == sol_len:
            return True
    return False


print(is_subsequence(s="", t="ahbgdc"))
print(is_subsequence(s="", t=""))
print(is_subsequence(s="abc", t="ahbgdc"))
print(is_subsequence(s="axc", t="ahbgdc"))
