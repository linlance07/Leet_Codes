class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        fair = [0]*k
        ans = float('inf')
        def spread(i):
            nonlocal fair,ans
            if i==len(cookies):
                ans = min(ans,max(fair))
                return
            if ans<max(fair):
                return
            for j in range(k):
                fair[j] += cookies[i]
                spread(i+1)
                fair[j] -= cookies[i]   
        spread(0)
        return ans
            