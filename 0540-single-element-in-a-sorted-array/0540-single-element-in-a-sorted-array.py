class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        p = 0
        for i in nums:
            p ^= i
        return p