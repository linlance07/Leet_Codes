#User function Template for python3

class Solution:
    def find_permutation(self, S):
        self.ans = []
        def perm(s,path):
            if not s:
                self.ans += [path]
            for i in range(len(s)):
                perm(s[:i]+s[i+1:],path+s[i])
        perm(S,"")
        return list(set(self.ans))
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S=input()
		ob = Solution()
		ans = ob.find_permutation(S)
		ans.sort()
		for i in ans:
			print(i,end=" ")
		print()
# } Driver Code Ends