class Solution:
    def jump(self, B: List[int]) -> int:
        l = 0
        r = B[0]
        ans = 1
        A = len(B)
        if A<=1:
            return 0
        while r<A-1:
            maxi = 0
            for j in range(l,r+1):
                maxi = max(maxi,j+B[j])
            if maxi==0 and r!=A-1:
                return -1
            ans += 1
            l = r
            r = maxi
        return ans