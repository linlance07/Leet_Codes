#User function Template for python3
class Solution:
	def addBinary(self, A, B):
		a = int(A,2)
		b = int(B,2)
		c = a + b
		return bin(c)[2:]
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		a,b = input().split(" ")
		ob = Solution()
		answer = ob.addBinary(a,b)
		
		print(answer)


# } Driver Code Ends