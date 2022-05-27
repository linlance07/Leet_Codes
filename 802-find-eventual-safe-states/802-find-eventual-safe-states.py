class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        O = defaultdict(list)
        I = defaultdict(list)
        Q = []
        for i in range(len(graph)):
            O[i] = len(graph[i])
            for j in graph[i]:
                I[j].append(i)
            if O[i]==0:
                Q.append(i)
        for k in Q:
            for x in I[k]:
                O[x] -= 1
                if O[x]==0:
                    Q.append(x)
        return sorted(Q)
            