class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        r = len(arr)-1
        m = 0
        while l<=r:
            mid = (l+r)//2
            curr = arr[mid] - mid - 1
            if curr<k:
                l = mid + 1
            else:
                r = mid - 1
        return k + l
            