from typing import List

"""
1. Greedy하게 풀면 안됨.
2. 값이 뒤로 갈 수 없다는것을 명심하면 한번에 풀 수 있는 문제다.
    - 뒤로 갈 수 없다는것은 [7,1,5,3,6,4] 에서 idx를 옮긴다 했을 때, 5 - 7과 같이 이미 지나온값과는 비교하지 않는다는것.
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy_day = float("inf")
        max_profit = 0
        for price in prices:
            if price < best_buy_day:
                best_buy_day = price
            elif price - best_buy_day > max_profit:
                max_profit = price - best_buy_day
        return max_profit

