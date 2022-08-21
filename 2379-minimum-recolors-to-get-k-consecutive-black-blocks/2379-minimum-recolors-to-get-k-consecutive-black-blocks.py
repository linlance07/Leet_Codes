class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        ans = float('inf')
        for i in range(len(blocks)-k+1):
            a = blocks[i:i+k]
            b = a.count('W')
            ans = min(ans,b)
        return ans