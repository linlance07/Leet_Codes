class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        D = defaultdict(list)
        for i,j in dislikes:
            D[i].append(j)
            D[j].append(i)
        C = defaultdict(lambda:None)
        def dfs(curr,c):
            if not C[curr]:
                C[curr] = c
            else:
                return C[curr]==c
            for x in D[curr]:
                if   not dfs(x,1 if c==2 else 2):
                    return False
            return True
        for i in range(1,n+1):
            if not C[i] and not dfs(i,1):
                return False
        return True