class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = []
        for i in range(32):
            for j in range(20):
                for k in range(14):
                    ugly.append(5**k*3**j*2**i)
        ugly.sort()
        return ugly[n-1]