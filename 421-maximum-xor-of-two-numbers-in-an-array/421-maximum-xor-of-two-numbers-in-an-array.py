class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans = 0
        mask = 0
        maxi = max(nums)
        n = len(bin(maxi)[2:])
        for i in range(n-1,-1,-1):
            mask |= (1<<i)
            pref = {mask & num for num in nums}
            print(mask,bin(mask)[2:])
            print(pref)
            
            t = ans | (1<<i)
            for p in pref:
                if p^t in pref:
                    ans = t
            print(ans,t)
        return ans