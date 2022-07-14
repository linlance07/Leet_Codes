class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        D = defaultdict(int)
        ans = 0
        for i in time:
            rem = -i % 60
            ans += D[rem]
            D[i%60] += 1
        return ans       