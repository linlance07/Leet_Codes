class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        ans = []
        for i in words:
            A = defaultdict(int)
            B = defaultdict(int)
            for j in range(len(i)):
                A[i[j]] = pattern[j]
                B[pattern[j]] = i[j]
            if list(A.keys())==list(B.values()):
                ans.append(i)
        return ans