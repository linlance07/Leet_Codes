class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = neg = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i]==0:
                pos = neg = 0
            elif nums[i]>0:
                pos += 1
                if neg==0:
                    neg = 0
                else:
                    neg += 1
            else:
                t = pos + 1
                if not neg:
                    pos = 0
                else:
                    pos = neg + 1
                neg = t
            ans = max(ans,pos)
        return ans
        
                