class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        print(nums)
        nums[:]=list(dict.fromkeys(nums))
        