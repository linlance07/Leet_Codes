class Solution:
    def findIntegers(self, n: int) -> int:
        fib = [1,2]
        for i in range(3,32):
            fib.append(fib[-1]+fib[-2])
        ans = 0
        act = 0
        for j in range(31,-1,-1):
            if (1<<j) & n:
                ans += fib[j]
                if act:
                    ans -= 1
                    break
                act = 1
            else:
                act = 0
        return ans+1
                