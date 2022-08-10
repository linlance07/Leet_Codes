class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        D = defaultdict(lambda:[0 for _ in range(len(votes[0]))])
        for i in votes:
            for j,k in enumerate(i):
                D[k][j] += 1
        A = sorted(D.keys())
        B = sorted(A,key = lambda x: D[x], reverse = True)
        return "".join(B)