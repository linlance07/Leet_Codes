class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        s = set()
        while nums:
            a = nums.pop(0)
            b = nums.pop()
            s.add((a+b)/2)
        return len(s)
            