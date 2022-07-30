class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        C = Counter()
        for i in B:
            C |= Counter(i)
        ans = []
        for j in A:
            if not C - Counter(j):
                ans.append(j)
        return ans