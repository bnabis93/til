import collections


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """s,t is isomorphic?
        isomorphic의 의미는 각 문자가 1-1대응으로 치환 될 수 있음을 의미한다.
        e.g. s = egg / t = add 인 경우 e - a / g - d로 mapping이 가능하고, egg를 mapping된 값으로 치환하면 agg가 나온다.
        s = foo / t = bar 인경우 f - b / o - a,r 로 매핑이 되므로 o에서 1-1대응이 깨져 isomorphic 하지 않다.

        풀이)
            - Dict 이용
            - greedy하게 하나씩 key mapping을 해주고, key 값이 2이상이면 false 반환
            - value를 비교 할 건데, 이미 같은 값이 존재한다면 egg의 g를 보면 될듯, pass 다른값인데 존재하면 false

        Solution tips
            - default dict 이용
        """


def is_isomorphic(s: str, t: str) -> bool:
    """."""
    solution_mapper = {}
    for idx, char in enumerate(s):
        if char in solution_mapper:
            if solution_mapper[char] != t[idx]:
                return False
        else:
            if t[idx] in solution_mapper.values():
                return False
            else:
                solution_mapper[char] = t[idx]

    return True


print(is_isomorphic(s="egg", t="add"))
print(is_isomorphic(s="foo", t="bar"))
print(is_isomorphic(s="badc", t="baba"))
print(is_isomorphic(s="aab", t="aaa"))
