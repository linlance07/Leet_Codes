class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        D = defaultdict(list)
        indegree = [0 for _ in range(n)]
        for i,j in edges:
            D[i].append(j)
            indegree[j] = 1
        Q = []
        for k in range(n):
            if indegree[k]==0:
                Q.append(k)
        visit = [0 for _ in range(n)]
        def dfs(x):
            visit[x] = 1
            for j in D[x]:
                if visit[j]==0:
                    dfs(j)
        ans = []
        for j in range(len(Q)):
            if visit[Q[j]]==0:
                ans.append(Q[j])
        return ans
            
            
            