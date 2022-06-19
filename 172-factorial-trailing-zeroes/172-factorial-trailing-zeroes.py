import math
class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        
        for i in range(0, n+1, 5):
            while i % 5 == 0 and i:
                i //= 5
                count += 1
                
        return count