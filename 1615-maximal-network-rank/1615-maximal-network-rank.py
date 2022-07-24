class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        G = defaultdict(set)
        for i,j in roads:
            G[i].add(j)
            G[j].add(i)
        ans = 0
        for i in range(n):
            for j in range(n):
                if i!=j:
                    ans = max(ans,len(G[i])+len(G[j])-(i in G[j]))
        return ans