class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

# 方法二(fast)#

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
# 方法三

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        di = dict()
        for i in s:
            if i not in di:
                di[i] = 1
            else:
                di[i] += 1
        for j in t:
            if j not in di:
                return False
            if j in di:
                di[j] -= 1
        for value in di.values():
            if value != 0:
                return False
        return True