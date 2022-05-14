class Solution:
	def sortedArrayToBST(self, nums):
	    arr = []
	    def bst(l,r):
            if l>r:
                return
            mid = (l+r)//2
            arr.append(nums[mid])
            bst(l,mid-1)
            bst(mid+1,r)
	    bst(0,len(nums)-1)
	    return arr
	        
	    # code here

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.sortedArrayToBST(nums)
		for _ in ans:
			print(_, end = " ")
		print()

# } Driver Code Ends