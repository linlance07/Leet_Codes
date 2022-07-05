class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = nums1 + nums2
        arr.sort()
        if len(arr)%2:
            return arr[len(arr)//2]
        a = len(arr)//2
        b = a - 1
        return (arr[b]+arr[a])/2