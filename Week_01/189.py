class Solution:
    def swap(self,nums: List[int], l: int, r: int) -> None: 
        while l < r:
            nums[r], nums[l] = nums[l], nums[r]
            l, r = l + 1, r - 1
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        self.swap(nums, 0, n-1)
        self.swap(nums, 0, k-1)
        self.swap(nums, k, n-1)
        """
        Do not return anything, modify nums in-place instead.
        """        
        