class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        G = defaultdict(lambda:None)
        for i in range(len(edges)):
            if edges[i]!=-1:
                G[i] = edges[i]
        vis = set()
        ans = 0
        def dfs(node,dis,D):
            nonlocal ans
            if node in vis:
                if node in D:
                    ans = max(ans,dis-D[node])
                return
            D[node] = dis
            vis.add(node)
            if G[node]!=None:
                dfs(G[node],dis+1,D)
        for i in range(len(edges)):
            if i not in vis:
                dfs(i,0,defaultdict(int))
        return ans if ans>0 else -1
        