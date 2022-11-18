class Solution:
    def isUgly(self, n: int) -> bool:
        x = 2**32
        for i in range(int(log(x,2))):
            for j in range(int(log(x,3))):
                for k in range(int(log(x,5))):
                    if n==(2**i)*(3**j)*(5**k):
                        return True
        return False