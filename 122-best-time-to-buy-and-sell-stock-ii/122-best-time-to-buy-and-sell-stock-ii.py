class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        l = 0
        r = 1
        while r<len(prices):
            dif = prices[r] - prices[l]
            if dif>0:
                ans += dif
                l = r
            else:
                l += 1
            r += 1
        return ans