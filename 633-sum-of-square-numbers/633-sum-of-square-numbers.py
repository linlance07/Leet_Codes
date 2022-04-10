class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(sqrt(c))
        while l<=r:
            ans = (l**2) + (r**2)
            if ans==c:
                return True
            if ans<c:
                l += 1
            else:
                r -= 1
        return False