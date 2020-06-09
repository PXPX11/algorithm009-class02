#调库法
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        return itertools.combinations([i for i in range(1,n+1)], k)

#回溯法
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(first = 1, curr = []):
            if len(curr) == k:
                output.append(curr[:])
                return
            for i in range(first, n+1):
                curr.append(i)
                backtrack(i+1, curr)
                curr.pop()
                
        output = []
        backtrack()
        return output