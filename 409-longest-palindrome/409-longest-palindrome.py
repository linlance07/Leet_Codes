class Solution:
    def longestPalindrome(self, s: str) -> int:
        D = Counter(s)
        ans = 0
        odd = 0
        for j in D:
            if D[j]%2==0:
                ans += D[j]
            else:
                odd = 1
                ans += D[j] - 1
        if odd:
            return ans + 1
        return ans