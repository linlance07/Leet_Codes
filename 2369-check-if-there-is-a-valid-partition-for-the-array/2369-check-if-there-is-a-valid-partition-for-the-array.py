class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        dp = [False,False,False,True]
        for i in range(len(nums)):
            dp[i%4] = False
            if i>0 and nums[i]==nums[i-1]:
                dp[i%4] |= dp[(i-2)%4]
            if i>1 and nums[i]==nums[i-1]==nums[i-2]:
                dp[i%4] |= dp[(i-3)%4]
            if i>1 and nums[i]==nums[i-1]+1==nums[i-2]+2:
                dp[i%4] |= dp[(i-3)%4]
        return dp[(len(nums)-1)%4]
        
                
                
                
            
            