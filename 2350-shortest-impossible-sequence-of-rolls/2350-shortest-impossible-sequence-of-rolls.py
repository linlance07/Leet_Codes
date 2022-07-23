class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        S = set()
        ans = 1
        for i in rolls:
            S.add(i)
            if len(S)==k:
                ans += 1
                S.clear()
        return ans
        