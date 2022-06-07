class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        if m==0:
            nums1[:] = nums2
        elif n==0:
            nums1 = nums1
        else:
            ans = []
            i,j = 0,0
            while i<m and j<n:
                if nums1[i]<=nums2[j]:
                    ans.append(nums1[i])
                    i+=1
                else:
                    ans.append(nums2[j])
                    j+=1
            if i!=m:
                ans+=nums1[i:m]
            if j!=n:
                ans+=nums2[j:n]
            nums1[:] = ans
                