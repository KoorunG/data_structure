# leet-code #42

# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# 주어진 그림에서 빗물을 얼마나 받을 수 있는가를 계산하라

# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# -> 0에서부터 x좌표가 1씩 증가하면서 배열의 요소만큼 y값이 매핑되는 형태..
# Output: 6
from typing import List

h1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
h2 = [4, 2, 0, 3, 2, 5]


# 1. 투 포인터 이용 : 거의 알아냈는데 max() 함수를 간과함..
# 파이썬의 max() 함수 : 인자가 두 개 이상 올 경우, 인자들 중 가장 큰 데이터를 반환함
# ex) a = [2, 3, 4]
#     b = [9, 8, 6, 1, 2]
#     c = [8, 10, 100 ,5, 5]
#     max(a, b, c) = [9, 8, 6, 1, 2]

# 1. 투 포인터 이용 : 117 ms	15.7 MB
def trap(height: List[int]) -> int:
    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    rain = 0

    while left < right:
        left_max, right_max = max(height[left], left_max), max(height[right], right_max)

        # 여기서 left, right가 아닌, left_max와 right_max값을 비교하여
        # 각 비교 대상보다 작은 동안 포인터를 이동시켜서 rain 값을 누적시킨다
        if left_max <= right_max:
            rain += left_max - height[left]
            left += 1
        else:
            rain += right_max - height[right]
            right -= 1
    return rain
# 왼쪽과 오른쪽에서 배열의 길이만큼 탐색을 해나가면서 계산하기 때문에 시간복잡도는 O(n)이다


# 2. 스택 이용
# def trap2(height: List[int]) -> int:
#     stack = []
#     rain = 0
#
#     # 배열의 길이만큼 반복
#     for i in range(len(height)):
#         # 변곡점을 만나는 경우(?)
#         while stack and height[i] > height[stack[-1]]:
#             # 스택에서 꺼냄
#             top = stack.pop()
#             # 스택에 값이 없다면 반복 중지
#             if not len(stack):
#                 break
#
#             distance = i - stack[-1] - 1
#             waters = min(height[i], height[stack[-1]]) - height[top]
#
#             rain += distance + waters
#
#         stack.append(i)
#     return rain


print(trap(h1))
print(trap(h2))