class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        prev_min = prices[0]
        for i in range(len(prices)):
            prev_min = min(prices[i], prev_min)
            max_profit = max(max_profit, prices[i] - prev_min)

        return max_profit