#User function Template for python3

class Solution:
	def MaxGold(self, matrix):
		rows = len(matrix)
		cols = len(matrix[0])
		ans = 0
		for i in range(rows):
		    for j in range(cols):
		        if i==0:
		            ans = max(ans,matrix[i][j])
		        else:
    		        if matrix[i][j]!=-1:
    		            x = y = z = -1
    		            y = matrix[i-1][j]
    		            if j!=0:
    		                x = matrix[i-1][j-1]
    		            if j!=cols-1:
    		                z = matrix[i-1][j+1]
    		            res = max(x,y,z)
    		            if res==-1:
    		                matrix[i][j] = -1
    		            else:
    		                matrix[i][j] += res
    		            ans = max(ans,matrix[i][j])
	    return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		m, n = input().split()
		m = int(m); n = int(n);
		matrix = []
		for _ in range(m):
			cur = list(map(int, input().split()))
			matrix.append(cur)
		obj = Solution()
		ans = obj.MaxGold(matrix)
		print(ans)

# } Driver Code Ends