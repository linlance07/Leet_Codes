class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        rows = len(image)
        cols = len(image[0])
        visit = set()
        def dfs(r,c,new,val):
            if (r,c) in visit or r<0 or r==rows or c<0 or c==cols or image[r][c]!=val:
                return
            visit.add((r,c))
            image[r][c] = new
            dfs(r+1,c,new,val)
            dfs(r-1,c,new,val)
            dfs(r,c+1,new,val)
            dfs(r,c-1,new,val)    
        dfs(sr,sc,newColor,image[sr][sc])
        return image
        
        
        
        
        