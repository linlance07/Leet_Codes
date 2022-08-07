class Solution:
    def countVowelPermutation(self, n: int) -> int:
        a = e = i = o = u = 1
        for x in range(n-1):
            a,e,i,o,u = e,a+i,a+e+o+u,i+u,a
        return (a+e+i+o+u) % (10**9+7)