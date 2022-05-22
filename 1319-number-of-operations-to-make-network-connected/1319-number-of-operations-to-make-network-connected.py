class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        node = [True for _ in range(n)]
        G = defaultdict(list)
        for j in range(len(connections)):
            a,b = connections[j]
            G[a].append(b)
            G[b].append(a)
        global avail
        free = set()
        avail = 0
        def dfs(q):
            global avail
            node[q] = False
            for _ in G[q]:
                if node[_]:
                    free.add((min(q,_),max(q,_)))
                    dfs(_)  
                else:
                    if (min(q,_),max(q,_)) not in free:
                        avail += 1
                        free.add((min(q,_),max(q,_)))
        count = 0
        for x in range(n):
            if node[x]:
                count += 1
                dfs(x)
        separate = count - 1
        print(avail,separate)
        if avail>= separate:
            return separate
        return -1
        