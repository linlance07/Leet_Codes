class Solution:
    def longestPalindrome(self, s: str) -> str:
        M = 0
        def check(l,r):
            res = ""
            while l>=0 and r<len(s) and s[l]==s[r]:
                l -= 1
                r += 1
            return s[l+1:r]
        ans = ""
        for i in range(len(s)):
            A = check(i,i)
            B = check(i,i+1)
            if len(A)>len(B):
                if len(A)>M:
                    M = len(A)
                    ans = A
            else:
                if len(B)>M:
                    M = len(B)
                    ans = B
        return ans