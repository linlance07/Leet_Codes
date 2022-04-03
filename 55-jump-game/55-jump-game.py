class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last = None
        for i in range(len(nums)-1,-1,-1):
            if last==None:
                last = i
            else:
                if i+nums[i]>=last:
                    last = i
        if last==0:
            return True
        return False