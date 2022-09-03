class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for i in range(1,n+1):
            a = bin(i)[2:]
            if a not in s:
                return False
        return True