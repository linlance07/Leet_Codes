class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        arr = sorted(nums,reverse = True)
        def check(L):
            if L[0]+L[1]>L[2] and L[1]+L[2]>L[0] and L[2]+L[0]>L[1]:
                return True
            return False
        for i in range(len(arr)-2):
            if check(arr[i:i+3]):
                return sum(arr[i:i+3])
        return 0