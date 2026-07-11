class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # Both pointers start together
        # Sliding Window
        left = 0
        right = 0

        max_profit = 0

        while right < len(prices):
            if prices[right] <= prices[left]:
                left = right
                right += 1
            else:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
                right += 1
        
        return max_profit