class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        D = defaultdict(int)
        n = len(nums1)
        for i in range(n):
            for j in range(n):
                D[nums1[i]+nums2[j]] += 1
        ans = 0
        for i in range(n):
            for j in range(n):
                ans += D[-nums3[i]-nums4[j]]
        return ans