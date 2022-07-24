class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        G = defaultdict(list)
        for i in range(len(graph)):
            G[i] = graph[i]
        C = defaultdict(lambda:None)
        def dfs(curr,c):
            if not C[curr]:
                C[curr] = c
            else:
                return C[curr]==c
            for x in G[curr]:
                if not dfs(x,not c):
                    return False
            return True
        for i in range(len(graph)):
            if not C[i] and not dfs(i,0):
                return False
        return True