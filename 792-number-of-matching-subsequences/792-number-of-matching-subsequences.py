class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        D = set()
        N = set()
        for w in words:
            i = 0
            j = 0
            if w in D:
                ans += 1
            elif w not in N:
                while i<len(s) and j<len(w):
                    if s[i]==w[j]:
                        j += 1
                    i += 1
                if j==len(w):
                    D.add(w)
                    ans += 1
                else:
                    N.add(w)
        return ans