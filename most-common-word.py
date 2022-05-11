# leet code #819

# 테스트케이스

# Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
# Output: "ball"
import collections
import re
from typing import List

s = "Bob hit a ball, the hit BALL flew far after it was hit."
b = ["hit"]

ss = "a"
bb = []

sss = "Bob!"
bbb = ["hit"]

ssss = "a, a, a, a, b,b,b,c, c"
bbbb = ["a"]


# 1. 내 풀이 -> 102 ms	14 MB
def mostCommonWord(paragraph: str, banned: List[str]) -> str:
    tmp_list = []
    tmp_list2 = []
    words = paragraph.split(' ')

    for word in words:
        if word.isalpha():
            tmp_list.append(word.lower())
        else:
            tmp_list2.append(word.lower())

    for wrong_word in tmp_list2:
        for char in wrong_word:
            if not char.isalpha():
                tmp_list3 = wrong_word.split(char)
                tmp_list3.remove('')
                tmp_list = tmp_list + tmp_list3
                break

    tmp_list4 = []
    list_length = len(tmp_list)
    for i in range(list_length):
        if tmp_list[i] not in banned:
            tmp_list4.append(tmp_list[i])

    return collections.Counter(tmp_list4).most_common(1)[0][0]


print(mostCommonWord(s, b))
print(mostCommonWord(ss, bb))
print(mostCommonWord(sss, bbb))
print(mostCommonWord(ssss, bbbb))


# 2. 리스트 컴프리헨션 이용 -> 49 ms	14 MB
def mostCommonWord2(paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    return collections.Counter(words).most_common(1)[0][0]


print(mostCommonWord2(s, b))
print(mostCommonWord2(ss, bb))
print(mostCommonWord2(sss, bbb))
print(mostCommonWord2(ssss, bbbb))


## 정규식과 리스트 컴프리헨션을 잘 익혀두도록 하자...