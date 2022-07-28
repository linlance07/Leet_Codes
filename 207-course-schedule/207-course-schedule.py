class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        G = defaultdict(list)
        vis = [0 for _ in range(numCourses)]
        for i,j in pre:
            G[j].append(i)
        def dfs(node):
            if vis[node]==1:
                return False
            if vis[node]==2:
                return True
            vis[node] = 1
            for nxt in G[node]:
                if not dfs(nxt):
                    return False
            vis[node] = 2
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True