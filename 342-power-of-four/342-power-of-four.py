class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n and not (n & n-1):
            if math.log2(n)%2==0:
                return True
        return False
            