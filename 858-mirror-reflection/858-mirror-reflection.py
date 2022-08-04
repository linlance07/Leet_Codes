class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        a = (p & -p) >= (q & -q)
        b = (p & -p) > (q & -q)
        return a + b