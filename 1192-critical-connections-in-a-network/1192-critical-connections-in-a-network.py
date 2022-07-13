class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        dis = [-1]*n
        low = [-1]*n
        seen = set()
        G = defaultdict(list)
        self.time = 0
        for i,j in connections:
            G[i] += [j]
            G[j] += [i]
        ans = []
        def dfs(curr,prev):
            seen.add(curr)
            self.time += 1
            dis[curr] = low[curr] = self.time
            for next in G[curr]:
                if next not in seen:
                    dfs(next,curr)                    
                    low[curr] = min(low[curr],low[next])
                elif next!=prev:
                    low[curr] = min(low[curr],dis[next])
                if low[next]>dis[curr]:
                    ans.append([curr,next])
        dfs(0,-1)
        return ans
            
            