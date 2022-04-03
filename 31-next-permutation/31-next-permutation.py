class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        l = None
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                l = i
                break
        r = None
        ma = 1000
        if l!=None:
            for j in range(l+1,len(nums)):
                if nums[j]>nums[l]:
                    if nums[j]<=ma:
                        ma = nums[j]
                        r = j
            nums[l],nums[r] = nums[r],nums[l]
        print(nums,l,r)
        if l==None:
            nums[:] = nums[::-1]
        else:
            nums[:] = list(nums[:l+1]) + list(nums[l+1:])[::-1]
        