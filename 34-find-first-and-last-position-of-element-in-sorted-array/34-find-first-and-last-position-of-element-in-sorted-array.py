class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        l = 0
        r = len(nums)-1
        L = R = -1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                L = mid
                r = mid - 1
            elif nums[mid]<target:
                l = mid + 1
            else:
                r = mid - 1
        if L==-1:
            return [-1,-1]
        ll = 0
        rr = len(nums)-1
        while ll<=rr:
            mid = (ll+rr)//2
            if nums[mid]==target:
                R = mid
                ll = mid + 1
            elif nums[mid]>target:
                rr = mid - 1
            else:
                ll = mid + 1
        if R==-1:
            return [-1,-1]
        return [L,R]
            