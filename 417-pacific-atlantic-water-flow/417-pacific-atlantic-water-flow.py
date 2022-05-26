class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        visit1 = set()
        D = defaultdict(lambda:0)
        def dfs(r,c,p):
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visit1:
                return
            if heights[r][c]>=p:
                visit1.add((r,c))
                D[(r,c)] += 1
                dfs(r,c+1,heights[r][c])
                dfs(r,c-1,heights[r][c])
                dfs(r+1,c,heights[r][c])
                dfs(r-1,c,heights[r][c])
        for i in range(rows):
            dfs(i,0,0)
        for j in range(cols):
            dfs(0,j,0)
        ans = []
        visit2 = set()
        #print(D.keys())
        def dfs2(r,c,p):
            if r<0 or r>=rows or c<0 or c>=cols or (r,c) in visit2:
                return
            if heights[r][c]>=p:
                visit2.add((r,c))
                D[(r,c)] += 1
                dfs2(r,c+1,heights[r][c])
                dfs2(r,c-1,heights[r][c])
                dfs2(r+1,c,heights[r][c])
                dfs2(r-1,c,heights[r][c])
        for i in range(rows):
            dfs2(i,cols-1,0)
        for j in range(cols):
            dfs2(rows-1,j,0)
        for k in D:
            if D[k]>1:
                ans.append(list(k))
        #print(D)
        return ans