class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxProfit = 0
        if n == 1:
            return 0
        i, j = 0, 1
        while j < n:
            profit = (prices[j] - prices[i])
            maxProfit = max(maxProfit, profit)
            if not prices[i] < prices[j]:
                i = j
            j += 1
        return maxProfit

        