class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices)<=1:
            return 0
        ans = 0
        mini = prices[0]
        for i in range(1,len(prices)):
            if prices[i]<mini:
                mini = prices[i]
            elif prices[i]>mini+fee:
                ans += prices[i] - mini - fee
                mini = prices[i] - fee
        return ans