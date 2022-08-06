class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        vis = set()
        nums.sort()
        for i in range(len(nums)):
            A = -nums[i]
            j = i+1
            k = len(nums)-1
            while j<k:
                if nums[j]+nums[k]<A:
                    j+=1
                elif nums[j]+nums[k]>A:
                    k-=1
                else:
                    if (nums[i],nums[j],nums[k]) not in vis:
                        ans.append([nums[i],nums[j],nums[k]])
                        vis.add((nums[i],nums[j],nums[k]))
                    j+=1
                    k-=1
        return ans