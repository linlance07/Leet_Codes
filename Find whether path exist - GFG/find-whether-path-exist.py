

class Solution:
    
    #Function to find whether a path exists from the source to destination.
	def is_Possible(self, grid):
		rows = len(grid)
		cols = len(grid[0])
		Q = []
		mat = [[True for _ in range(cols)] for __ in range(rows)]
		for i in range(rows):
		    for j in range(cols):
		        if grid[i][j]==1:
		            Q.append((i,j))
		ans = 0
		D = [(1,0),(-1,0),(0,1),(0,-1)]
	    while Q:
	        q = Q.pop(0)
	        #print(q)
	        for _ in D:
	            r = q[0] + _[0]
	            c = q[1] + _[1]
	            if r>=0 and r< rows and c>=0 and c<cols and grid[r][c]>=2 and mat[r][c]:
	                mat[r][c] = False
	                if grid[r][c]==2:
	                    #print((r,c))
	                    ans = 1
	                    break
	                Q.append((r,c))
	        if ans:
	            break
        return ans
	                
	        

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		grid = []
		for _ in range(n):
			a = list(map(int, input().split()))
			grid.append(a)
		obj = Solution()
		ans = obj.is_Possible(grid)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends