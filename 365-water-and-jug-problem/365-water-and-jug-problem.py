class Solution:
    def canMeasureWater(self, a: int, b: int, c: int) -> bool:
        g = gcd(a,b)
        if g==0:
            if c==0:
                return True
            return False
        if a+b>=c and c%g==0:
            return True
        return False