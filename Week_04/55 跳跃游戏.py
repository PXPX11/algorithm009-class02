class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if nums == [0]:return True
        maxi = 0
        endindex = len(nums) - 1
        for i, v in enumerate(nums):
            if maxi >= i and i +v > maxi:
                maxi = i +v
                if maxi >= endindex:
                    return True
        return False