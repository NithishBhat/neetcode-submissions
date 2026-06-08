class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxLen=0
        for buy in range(len(prices)):
            for sell in range(buy+1,len(prices)):
                maxLen=max(maxLen,prices[sell]-prices[buy])
                
        return maxLen