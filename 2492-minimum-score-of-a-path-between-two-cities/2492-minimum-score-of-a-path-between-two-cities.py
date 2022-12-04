class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        ans = float('inf')
        G = defaultdict(list)
        for i,j,k in roads:
            G[i] += [(j,k)]
            G[j] += [(i,k)]
        vis = set()
        def dfs(node):
            nonlocal ans
            if node in vis:
                return
            vis.add(node)
            for nxt,val in G[node]:
                ans = min(ans,val)
                dfs(nxt)
        dfs(1)
        return ans
            
        