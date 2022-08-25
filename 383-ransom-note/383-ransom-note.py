class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        D = dict(Counter(magazine))
        for j in ransomNote:
            if D.get(j,0)<=0:
                return False
            D[j] = D.get(j,0)-1
        return True