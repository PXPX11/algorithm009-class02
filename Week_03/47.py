#调库
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return set(itertools.permutations(nums,len(nums)))

#自己写的方法(时间巨长)
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums,visted,subset):
            if len(subset)==len(nums):
                res.append(subset)
                return
            for i in range(len(nums)):
                if i not in visted:
                    visted.add(i)
                    backtrack(nums,visted, subset + [nums[i]])
                    visted.remove(i)
                        
        visted = set()        
        res = []
        backtrack(nums,visted,[])
        ans = []
        for l in res:
            if l not in ans:
                ans += [l]
        return ans