class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        res = 0
        while j < len(prices):
            newMax = prices[j] - prices[i]
            res = max(res, newMax)
            if prices[i] > prices[j]:
                i = j
                j += 1
            elif prices[i] <= prices[j]:
                j += 1
        return res