 class Solution:
        def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        ans = 0
        l, r = 0, len(height) - 1
        leftmax, rightmax = height[l], height[r]
        while l < r:
            leftmax, rightmax = max(leftmax, height[l]), max(rightmax, height[r])
            if leftmax < rightmax:
                ans += (leftmax - height[l])
                l += 1
            else: 
                ans += (rightmax - height[r])
                r -= 1
        return ans

# 在分析解法后 我自己还是看不太懂 stack 的解法, 请帮我分析一下好么?