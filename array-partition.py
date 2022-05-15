# leet-code #561

# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
# -> 요소가 짝수개인 배열이 주어졌다. 한 쌍씩 묶어서 min값을 구한 뒤 그 결과의 합이 최대인 경우 합을 출력해라

# Input: nums = [1,4,3,2]
# Output: 4
# Explanation: All possible pairings (ignoring the ordering of elements) are:
# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# So the maximum possible sum is 4.
from typing import List

nums = [6, 2, 6, 5, 1, 2]


# 1. 내 풀이 : 333 ms	16.1 MB
# 배열을 정렬한 뒤, pop으로 꺼낸 값을 min으로 비교하여 더하면 최댓값이 나옴
def arrayPairSum(nums: List[int]) -> int:
    result = 0
    nums.sort()
    while len(nums) != 0:
        result += min(nums.pop(), nums.pop())
    return result


# print(arrayPairSum(nums))


# 2. 정렬된 상태에서 짝수번째의 값이 항상 작음을 이용 : 392 ms	16.8 MB
def arrayPairSum2(nums: List[int]) -> int:
    return sum(sorted(nums)[::2])


print(arrayPairSum2(nums))

