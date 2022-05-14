# leet-code #15

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
# -> 서로 인덱스가 같이 않으면서 합이 0인 세 수를 출력하라 단, 중복되는 배열을 리턴하면 안된다.

# 테스트 케이스
# Input: nums = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]
from typing import List

n1 = [-1, 0, 1, 2, -1, -4]
n2 = []
n3 = [0]
n4 = [-2, 0, 1, 1, 2]


# 1. 브루트포스 : 시간초과.. (O(n^3)이므로)
def threeSum(nums: List[int]) -> List[List[int]]:
    result = []

    # 요소가 3개 미만인 경우 빈 배열 리턴
    if len(nums) < 3:
        return result

    # 브루트포스로 처리 : O(n^3)
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    tmp_list = [nums[i], nums[j], nums[k]]
                    tmp_list.sort()
                    if tmp_list not in result:
                        result.append(tmp_list)

    return result


# 2. 투 포인터 : 802 ms	18.1 MB
# sum = 0이어서 진행이 안되는 상태일 경우의 스킵처리를 하는 부분을 잘 알아두자
def threeSum2(nums: List[int]) -> List[List[int]]:
    result = []
    # 요소가 3개 미만인 경우 빈 배열 리턴
    if len(nums) < 3:
        return []

    nums.sort()  # [-1, 0, 1, 2, -1, -4] -> [-4, -1, -1, 0, 1, 2]

    # for문으로 i를 돌리면서
    for i in range(len(nums) - 2):

        # nums[i]가 중복값인 경우 체크할 필요가 없으므로 건너뛰기
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # i 바로 앞에서 left를 시작하고 배열의 맨 끝에서 right를 시작하여 조건을 체크한다
        left, right = i + 1, len(nums) - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                left += 1
                right -= 1
    return result

print(threeSum2(n4))

# [-1, 0, 1, 2, -1, -4]
#   [-4, -1, -1, 0, 1, 2]
# [-2, 0, 1, 1, 2]