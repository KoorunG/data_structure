import collections
import re

inp = 'A man, a plan, a canal: Panama'
inp2 = 'race a car'


# 1. 내 풀이
def is_palindrome(s: str) -> bool:
    b = []
    c = []  # 빈 배열을 만들고
    for i, data in enumerate(s):
        if data.isalnum():  # isalnums() 메소드를 이용하여 영문자, 숫자 여부를 하나하나 체크
            b.append(data.lower())

    for i, data in enumerate(s[::-1]):  # 슬라이싱을 이용하여 문자열 뒤집음
        if data.isalnum():
            c.append(data.lower())

    return b == c  # 비교값 리턴


print(is_palindrome(inp))  # 60ms 소요


# 2. 데크 자료형 이용

def is_palindrome2(s: str) -> bool:
    # 자료형 데크로 선언
    from typing import Deque
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs) > 1:
        if strs.popleft() != strs.pop():  # Deque의 popleft()는 왼쪽에서 바로 추출하므로 O(1)이다
            return False
    return True


print(is_palindrome2(inp))  # 85ms 소요


# 3. 정규식 이용

def is_palindrome3(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)  # 정규식을 이용하여 문자 하나하나가 아닌 문자열 전체를 한번에 비교하여 치환했다.
    return s == s[::-1]


print(is_palindrome3(inp))  # 52ms 소요
