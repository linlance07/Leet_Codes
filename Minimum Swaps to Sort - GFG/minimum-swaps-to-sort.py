

class Solution:
    
    #Function to find the minimum number of swaps required to sort the array.
	def minSwaps(self, nums):
		A = sorted(nums)
		D = {}
		for i in range(len(nums)):
		    D[nums[i]] = i
		ans = 0
		for j in range(len(nums)):
		    if nums[j]!=A[j]:
		        ans += 1
		        a = D[nums[j]]
		        b = D[A[j]]
		        D[A[j]] = a
		        D[nums[j]] = b
		        nums[a],nums[b] = nums[b],nums[a]
		return ans

#{ 
#  Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		obj = Solution()
		ans = obj.minSwaps(nums)
		print(ans)

# } Driver Code Ends