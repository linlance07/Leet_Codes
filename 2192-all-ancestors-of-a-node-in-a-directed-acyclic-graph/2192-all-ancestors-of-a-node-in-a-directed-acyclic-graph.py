class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        G = defaultdict(list)
        for i,j in edges:
            G[i].append(j)
        ans = [[] for _ in range(n)]
        def dfs(prev,curr):
            for _ in G[curr]:
                if ans[_] and ans[_][-1]==prev:
                    continue
                ans[_].append(prev)
                dfs(prev,_)
        for k in range(n):
            dfs(k,k)
        return ans
                
                
        
        