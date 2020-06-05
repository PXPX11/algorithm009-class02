#双指针+ hash 表
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] +nums[j] == target:
                    return[i,j]
#速度太慢O(n^2)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = dict()
        for i, v in enumerate(nums):
            remain = target - v
            if remain in d:
                return [i,d.get(remain)]
            else:
                d[v] = i 
