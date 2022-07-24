class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [-1]*n
        G = defaultdict(list)
        vis = set()
        for i,j in redEdges:
            G[i].append((j,'r'))
        for i,j in blueEdges:
            G[i].append((j,'b'))
        vis.add((0,'r'))
        vis.add((0,'b'))
        Q = [(0,'r'),(0,'b')]
        step = 0
        while Q:
            n = len(Q)
            for _ in range(n):
                node,color = Q.pop(0)
                if ans[node]==-1:
                    ans[node] = step
                else:
                    ans[node] = min(ans[node],step)
                for nxt,clr in G[node]:
                    if color!=clr and (nxt,clr) not in vis:
                        Q.append((nxt,clr))
                        vis.add((nxt,clr))
            step += 1
        return ans
            
        