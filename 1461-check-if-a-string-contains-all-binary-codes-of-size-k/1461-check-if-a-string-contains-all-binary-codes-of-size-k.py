class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        S = set()
        for i in range(len(s)-k+1):
            S.add(s[i:i+k])
            if len(S)==2**k:
                break
        return len(S)==2**k