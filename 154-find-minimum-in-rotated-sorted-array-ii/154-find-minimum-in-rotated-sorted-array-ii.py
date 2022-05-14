class Solution:
    def findMin(self, nums: List[int]) -> int:
        arr = []
        for i in nums:
            if arr:
                if arr[-1]!=i:
                    arr.append(i)
            else:
                arr.append(i)
        nums[:] = arr
        l = 0
        r = len(nums) - 1
        while l<r:
            mid = (l+r)//2
            if nums[mid]<nums[r]:
                r = mid
            else:
                l = l + 1
        return nums[l]