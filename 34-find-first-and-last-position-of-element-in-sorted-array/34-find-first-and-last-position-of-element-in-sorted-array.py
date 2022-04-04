class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid]<target:
                l = mid + 1
            else:
                r = mid
        if nums[l]!=target:
            return [-1,-1]
        ll = 0
        rr = len(nums)-1
        while ll<rr:
            mid = (ll+rr)//2+1
            if nums[mid]>target:
                rr = mid - 1
            else:
                ll = mid
        if nums[ll]!=target:
            return [-1,-1]
        return [l,ll]
            