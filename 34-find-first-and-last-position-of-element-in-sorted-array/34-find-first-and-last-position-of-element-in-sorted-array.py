class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        l = 0
        r = len(nums)-1
        L,R = None,None
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                L = mid
                r = mid - 1
            elif nums[mid]>target:
                r = mid - 1
            else:
                l = mid + 1
        l = 0
        r = len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                R = mid
                l = mid + 1
            elif nums[mid]<target:
                l = mid + 1
            else:
                r = mid - 1
        if L!=None and R!=None:
            return [L,R]
        return [-1,-1]
            