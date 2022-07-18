class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        D = defaultdict(int)
        D[0] = 1
        for j in nums:
            ans += D[j%k]
            D[j%k] += 1
        return ans
            
            
            