class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        nodes = [True for _ in range(len(isConnected))]
        G = defaultdict(list)
        n = len(isConnected)
        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    G[i].append(j)
        ans = 0
        def dfs(q):
            nodes[q] = False
            for _ in G[q]:
                if nodes[_]:
                    dfs(_)
        for Q in range(n):
            if nodes[Q]:
                ans += 1
                dfs(Q)
        return ans