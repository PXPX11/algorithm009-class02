class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack (nums,visted,subset):
            if len(subset) == len(nums):
                res.append(subset)
            for i in range(len(nums)):
                if i not in visted:
                    visted.add(i)
                    backtrack(nums,visted,subset + [nums[i]])
                    visted.remove(i)
        visted = set()
        res = []
        backtrack(nums,visted,[])
        return res

#调库
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return itertools.permutations(nums,len(nums))
