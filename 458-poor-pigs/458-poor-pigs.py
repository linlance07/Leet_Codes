class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        rounds = minutesToTest // minutesToDie
        ans = 0
        while (rounds+1)**ans < buckets:
            ans += 1
        return ans