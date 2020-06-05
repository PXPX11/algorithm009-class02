#类似于大顶堆, 在每次 nums[i] 和 2,3,5 依次相乘时比较大小而且依次进入结果的 list 
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        i2 = 0
        i3=0
        i5=0
        for _ in range(n-1):
            v = min(nums[i2] *2, nums[i3] *3, nums[i5] *5)
            nums.append(v)
            while nums[i2] *2 <= v:
                i2 += 1
            while nums[i3] *3<= v:
                i3 += 1
            while nums[i5] *5<= v:
                i5 += 1
        return nums[-1]
