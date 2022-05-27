class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        G = defaultdict(list)
        roads = set()
        for i,j in connections:
            roads.add((i,j))
            G[i].append(j)
            G[j].append(i)
        global ans
        ans = -1
        def dfs(c,p):
            global ans
            if (c,p) not in roads:
                ans += 1
            for _ in G[c]:
                if _ != p:
                    dfs(_,c)
        dfs(0,-1)
        return ans