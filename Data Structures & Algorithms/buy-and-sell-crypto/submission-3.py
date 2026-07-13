class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minp = prices[0]
        maxp = 0

        for price in prices:
            minp = min(minp,price)
            profit = price - minp
            maxp = max(maxp, profit)
        
        return maxp