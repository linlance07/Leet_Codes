class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        nums = list(set(nums))
        ans = 0
        s = []
        for i in range(len(nums)):
            a = bin(nums[i])[2:]
            b = a.count('1')
            s.append(b)
        s.sort()
        for j in range(len(s)):
            if k-s[j]<=s[j]:
                ind = bisect_left(s,k-s[j])
                ans += (j-ind)*2
                ans += 1
        return ans