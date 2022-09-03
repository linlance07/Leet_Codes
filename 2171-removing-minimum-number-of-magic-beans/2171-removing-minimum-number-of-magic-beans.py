class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        s = sum(beans)
        n = len(beans)
        ans = float('inf')
        for i in beans:
            ans = min(ans,s-n*i)
            n -= 1
        return ans