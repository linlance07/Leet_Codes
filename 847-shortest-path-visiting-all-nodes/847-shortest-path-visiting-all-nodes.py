class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        vis = set()
        final = (1<<len(graph)) - 1
        Q = [(i,1<<i) for i in range(len(graph))]
        ans = 0
        while Q:
            n = len(Q)
            for _ in range(n):
                node,state = Q.pop(0)
                if state==final:
                    return ans
                for nxt in graph[node]:
                    if (nxt,state|(1<<nxt)) not in vis:
                        vis.add((nxt,state|(1<<nxt)))
                        Q.append((nxt,state|(1<<nxt)))
            ans += 1