class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(n)]
        for i,j in edges:
            indegree[j] = 1
        Q = []
        for k in range(n):
            if indegree[k]==0:
                Q.append(k)
        return Q
            
            
            