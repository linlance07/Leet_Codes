class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        D = defaultdict(int)
        ans = 0
        for i in range(len(nums)):
            if k - nums[i] in D:
                ans += 1
                D[k-nums[i]] -= 1
                if D[k-nums[i]]==0:
                    del D[k-nums[i]]
            else:
                D[nums[i]] += 1
            #print(D)
        return ans