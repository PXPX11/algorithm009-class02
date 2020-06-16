class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums) - 1
        maxp, end, step = 0,0,0
        for i in range(n):
            if maxp >= i:
                maxp = max(maxp, nums[i] + i)
                if i == end:
                    end = maxp
                    step += 1
        return step

#在每次可跳的范围内选择最远的位置