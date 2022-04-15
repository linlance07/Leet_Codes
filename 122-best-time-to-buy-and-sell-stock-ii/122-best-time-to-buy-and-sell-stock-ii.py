class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        ans = 0
        while r<len(prices):
            if prices[r]>prices[l]:
                ans += prices[r] - prices[l]
                l = r
            else:
                l += 1
            r += 1
        return ans