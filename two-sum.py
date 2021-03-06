# leet-code #1

# 덧셈하여 타겟을 만들 수 있는 두 수를 출력하라

# 테스트 케이스
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]


# 1. 내 풀이 : 타겟에서 한 수를 빼면 나머지 한 수가 나오는 경우를 찾는다
from typing import List

nums = [2, 7, 11, 15]
target = 9

nums2 = [3, 2, 4]
target2 = 6

nums3 = [3, 3]
target3 = 6


# 1. 내 풀이 : 114 ms	15.1 MB
def twoSum(nums: List[int], target: int) -> List[int]:
    # 딕셔너리는 해시테이블로 구현되어있기 때문에 O(1)로 조회가 가능하다
    tmp_dict = {}

    # 값을 key, 인덱스를 value로 바꿔서 저장한 뒤
    for i, n in enumerate(nums):
        tmp_dict[n] = i

    # target - n이 딕셔너리에 존재하고 서로의 인덱스가 다르다면 값을 리턴한다
    for i, n in enumerate(nums):
        if target - n in tmp_dict and i != tmp_dict[target - n]:
            return [i, tmp_dict[target - n]]


# 2. 투 포인터 이용 : 인덱스가 뒤죽박죽이 되기 때문에 풀이 불가
# (인덱스가 아닌, 값을 리턴하는 문제였다면 매우 쉽게 풀렸을거임)
def twoSum2(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while not left == right:
        if nums[left] + nums[right] < target:
            left += 1
        elif nums[left] + nums[right] > target:
            right -= 1
        else:
            return [left, right]


print(twoSum(nums, target))
print(twoSum(nums2, target2))
print(twoSum(nums3, target3))

print(twoSum2(nums, target))
print(twoSum2(nums2, target2))
print(twoSum2(nums3, target3))
