class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        Q = []
        ans = []
        if len(nums)==k:
            return [max(nums)]
        for i in range(len(nums)):
            if i<k:
                if Q:
                    while Q and Q[-1][0]<nums[i]:
                        Q.pop()
                    Q.append((nums[i],i))                
                else:
                    Q.append((nums[i],i))
            else:
                if i==k:
                    ans.append(Q[0][0])
                if i-Q[0][1]>=k:
                    Q.pop(0)
                while Q and Q[-1][0]<nums[i]:
                    Q.pop()
                Q.append((nums[i],i))
                #print(Q)
                ans.append(Q[0][0])
        return ans