# leet code #49

# 테스트 케이스

# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
import collections
from typing import List

s = ["eat", "tea", "tan", "ate", "nat", "bat"]


# 1. 첫 풀이 -> 시간초과
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    result = []
    tmp_keys = []
    tmp_values = []
    for word in strs:
        tmp_list = []
        tmp_string = ''

        for char in word:
            tmp_list.append(char)
            tmp_list.sort()
        for char2 in tmp_list:
            tmp_string += char2
        tmp_keys.append(tmp_string)
        tmp_values.append(word + '>' + tmp_string)

    for key in set(tmp_keys):
        tmp_result = []
        for value in tmp_values:
            # print(value)
            value_split = value.split('>')
            if key in value_split:
                tmp_result.append(value_split[0])
        result.append(tmp_result)
    return result


# print(groupAnagrams(s))


# 2. 두번째 풀이 -> 165 ms	17.1 MB
def groupAnagrams2(strs: List[str]) -> List[List[str]]:
    result = collections.defaultdict(list)  # key값이 없을 때 디폴트값인 []를 딕셔너리의 키로 지정

    for word in strs:
        result[''.join(sorted(word))].append(word)  # 인자값이 list라고 명시된 상태이기 때문에 append() 함수를 바로 쓸 수 있는 것

    return list(result.values())


print(groupAnagrams2(s))
