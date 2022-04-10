class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        D = dict(Counter(nums1))
        ans = []
        for i in nums2:
            if i in D and D[i]>0:
                ans.append(i)
                D[i]-=1
        return ans