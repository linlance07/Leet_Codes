class Solution:
    def firstUniqChar(self, s: str) -> int:
        D = Counter(s)
        for i,j in enumerate(s):
            if D[j]==1:
                return i
        return -1