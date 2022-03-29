class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        for i in range(n):
            nums[nums[i]%n]+=n
        for i in range(n):
            if (nums[i]//n)>1:
                return i
        