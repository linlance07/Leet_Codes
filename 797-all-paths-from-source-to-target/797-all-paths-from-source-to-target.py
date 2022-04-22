class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        G = defaultdict(list)
        for i in range(len(graph)):
            G[i] += graph[i]
        ans = []
        def dfs(q,path):
            if q==len(G)-1:
                ans.append(path)
                return
            for i in G[q]:
                dfs(i,path+[i])      
        dfs(0,[0])      
        return ans