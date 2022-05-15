# leet-code #238

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# -> 자기 자신을 제외한 배열 요소의 모든 곱을 인자로 하는 배열을 출력해라
# -> 시간복잡도는 O(n)을 넘어가서는 안된다

# 테스트 케이스

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
import collections
from typing import List

n1 = [1, 2, 3, 4]
n2 = [-1, 1, 0, -3, 0, 3]


# 내 풀이 : 425 ms	21.6 MB
# 맞긴 한데 정리가 너무 덜 되어있음..
def productExceptSelf(nums: List[int]) -> List[int]:
    tmp_lst = nums[::]
    tmp = nums[0]
    result = []
    zero_idx = []
    # if 0 in nums:
    #     nums.remove(0)
    #     nums.remove(0)

    for i in range(len(nums)):
        if nums[i] == 0:
            nums[i] = 1
            zero_idx.append(i)

    if len(zero_idx) > 1:
        return [0 for n in nums]


    for i in range(len(nums)):
        if i != len(nums) - 1:
            tmp = tmp * nums[i + 1]
    tmp_result = [tmp // n for n in nums]

    if 0 in tmp_lst:
        for i in range(len(nums)):
            if i in zero_idx:
                tmp_result[i] = tmp
            else:
                tmp_result[i] = 0
        # tmp_result.insert(idx, 0)
    return tmp_result

# print(productExceptSelf(n1))
print(productExceptSelf(n2))


