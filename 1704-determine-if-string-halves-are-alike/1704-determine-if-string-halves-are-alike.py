class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        a = b = 0
        for i in range(n):
            if s[i] in "aeiouAEIOU":
                if i<(n//2):
                    a += 1
                else:
                    b += 1
        return a==b