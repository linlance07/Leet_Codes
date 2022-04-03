class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        l = None
        r = None
        for i in range(len(nums)-1,0,-1):
            if nums[i-1]<nums[i]:
                l = i - 1
                break
        if l!=None:
            ma = 1000
            for j in range(l+1,len(nums)):
                if nums[j]>nums[l]:
                    if nums[j]<=ma:
                        r = j
            nums[l],nums[r] = nums[r],nums[l]
            nums[:] = nums[:l+1] + (nums[l+1:])[::-1]            
        else:
            nums[:] = nums[::-1]
        
                
        