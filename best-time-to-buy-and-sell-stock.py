# leet-code #121

# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# 테스트 케이스

# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
import sys
from typing import List

p1 = [7, 1, 5, 3, 6, 4]
p2 = [7, 6, 4, 3, 1]
p3 = [2, 1]
p4 = [1, 2, 1]
p5 = [2, 2, 5]
p6 = [2, 1, 2, 0, 1]
p7 = [2, 4, 1]

# 1. 배열을 훑어가며 현재점, 저점, 고점을 비교 및 갱신 후 계산 : 1630 ms	25 MB
class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_price = 0
        min_price = sys.maxsize # 최솟값의 초기값은 시스템의 최대 숫자로 설정, 어차피 바로 초기화 될 예정

        # 최솟값과 최댓값을 계속 갱신
        for price in prices:
            min_price = min(min_price, price)
            max_price = max(max_price, price - min_price)

        return max_price

solution = Solution()

print(solution.maxProfit(p1))
print(solution.maxProfit(p2))
print(solution.maxProfit(p3))
print(solution.maxProfit(p4))
print(solution.maxProfit(p5))
print(solution.maxProfit(p6))
print(solution.maxProfit(p7))
