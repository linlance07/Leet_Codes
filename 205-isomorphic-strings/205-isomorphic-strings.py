class Solution:
    def isIsomorphic(self, pattern: str, s: str) -> bool:
        P = {}
        S = {}
        if len(pattern)!=len(s):
            return False
        for i in range(len(pattern)):
            P[pattern[i]] = s[i]
            S[s[i]] = pattern[i]
        if list(P.keys())!=list(S.values()):
            return False
        return True