class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        nums = nums + nums
        arr = []
        cc = c = 0
        for i in range(n):
            if nums[i]:
                cc += 1
        for k in nums:
            if k:
                c += 1
            arr.append(c)
        #print(cc,c,nums,arr)
        l = 0
        r = cc - 1
        one = arr[r]
        ans = cc - one
        for j in range(cc,len(arr)):
            r = j
            one = arr[r] - arr[l]
            l += 1
            ans = min(ans,cc - one)   
        return ans
            
            