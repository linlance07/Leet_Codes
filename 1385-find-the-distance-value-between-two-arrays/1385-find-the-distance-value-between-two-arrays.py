class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0
        for i in arr1:
            l = 0
            r = len(arr2)-1
            while l<=r:
                mid = (l+r)//2
                if abs(arr2[mid]-i)<=d:
                    ans -= 1
                    break
                if arr2[mid]>i:
                    r = mid - 1
                else:
                    l = mid + 1   
            ans += 1
        return ans