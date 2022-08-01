class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        seen = {0}
        s = 0
        ans = 0
        for i in nums:
            s += i
            a = s - target
            if a in seen:
                ans += 1
                seen = set()
            seen.add(s)
        return ans