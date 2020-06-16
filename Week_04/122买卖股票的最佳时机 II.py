#方法一
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            if prices[i] <= prices[i+1]:
                profit = profit + prices[i+1] - prices[i]
        return profit
#一行代码
        return sum(prices[i]-prices[i-1] for i in range(1,len(prices)) if prices[i]-prices[i-1]>0)
