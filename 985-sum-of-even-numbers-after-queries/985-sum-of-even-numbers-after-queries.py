class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        s = 0
        for i in nums:
            s += i if i%2==0 else 0
        ans = []
        for i,j in queries:
            a = nums[j]
            if a%2:
                nums[j] += i
                if nums[j]%2==0:
                    s += nums[j]
            else:
                s -= nums[j]
                nums[j] += i
                if nums[j]%2==0:
                    s += nums[j]
            ans += [s]
        return ans
                