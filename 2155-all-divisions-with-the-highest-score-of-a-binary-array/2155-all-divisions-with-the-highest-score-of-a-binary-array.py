class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        zero = one = 0
        for i in nums:
            if i:
                one += 1
        ans = [[0],one]
        D = defaultdict(list)
        D[one].append(0)
        for j in range(len(nums)):
            if nums[j]==0:
                zero += 1
            else:
                one -= 1
            s = zero + one
            D[s].append(j+1)
        arr = list(D.keys())
        M = max(arr)
        for k in D:
            if k==M:
                return D[k]
                
        