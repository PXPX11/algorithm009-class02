#方法一
class Solution:
    def findMin(self, nums: List[int]) -> int:
        return sorted(nums)[0]

#方法二
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] > nums[right]:         
                left = mid + 1
            else:                               
                right = mid
        return nums[left]

