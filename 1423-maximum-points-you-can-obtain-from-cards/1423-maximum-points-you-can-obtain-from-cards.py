class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        A = sum(cardPoints[:k])
        ans = A
        j = -1
        for i in range(k-1,-1,-1):
            A = A-cardPoints[i]+cardPoints[j]
            ans = max(ans,A)
            j-=1
        return ans