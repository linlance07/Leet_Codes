class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        unique = [0]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                unique.append(unique[-1]+1)
            else:
                unique.append(unique[-1])
        return sum(unique)
        
            
            