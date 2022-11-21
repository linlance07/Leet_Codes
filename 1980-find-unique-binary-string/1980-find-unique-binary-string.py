class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        s = set(nums)
        x = 0
        y = "0"*n
        while y in s:
            x += 1
            y = bin(x)[2:]
            y = '0'*(n-len(y)) + y
        return y
        