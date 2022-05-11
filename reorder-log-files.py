# leet_code #937

# 테스트 케이스

# Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
# Explanation:
# The letter-log contents are all different, so their ordering is "art can", "art zero", "own kit dig". -> 문자 로그가 모두 다르기 때문에 사전순 정렬
# The digit-logs have a relative order of "dig1 8 1 5 1", "dig2 3 6".   -> 숫자 로그는 입력받은 순서대로 출력

# Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
# Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
from typing import List

s = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
ss = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
sss = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo", "a2 act car"]


def reorderLogFiles2(logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 파이썬의 sort에는 key값을 전달할 수 있다.
    # 키값으로는 함수 (혹은 람다식) 등을 전달할 수 있다.
    # 파이썬은 lambda 키워드를 이용하여 람다식을 작성하는 것도 가능하다
    letters.sort(key=lambda x: (x.split()[1], x.split()[0]))
    return letters + digits


print(reorderLogFiles2(sss))