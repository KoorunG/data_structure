# 테스트 케이스
# Input: s = ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
#
# Input: s = ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
from typing import List

t = ["h", "a", "n", "n", "a", "H"]


# 1. 내 풀이
def reverseString(s: List[str]) -> None:
    for i in range(0, len(s) // 2):
        tmp = s[i]
        s[i] = s[len(s) - (i + 1)]
        s[len(s) - (i + 1)] = tmp


reverseString(t)  # 246 ms / 18.6 MB
print(t)          # 검증


# 2. 파이썬 슬라이싱 사용
def reverseString2(s: List[str]) -> None:
    s[:] = s[::-1]


reverseString2(t)  # 264 ms / 18.7 MB
print(t)           # 검증


# 3. 투 포인터
def reverseString3(s: List[str]) -> None:
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]   # 한 줄에 같이 쓰면 굳이 임시로 값을 담아두지 않아도 된다?
        left += 1
        right -= 1


reverseString3(t)  # 271 ms / 18.4 MB
print(t)           # 검증