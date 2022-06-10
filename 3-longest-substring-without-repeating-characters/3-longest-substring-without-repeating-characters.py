class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        D = {}
        st = 0
        ans = 0
        for i in range(len(s)):
            if s[i] in D and D[s[i]]>=st:
                st = D[s[i]]+1
            ans = max(ans,i-st+1)
            D[s[i]] = i
        return ans