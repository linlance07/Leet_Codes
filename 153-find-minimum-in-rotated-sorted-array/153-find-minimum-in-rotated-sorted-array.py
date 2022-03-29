class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        self.ind = float('inf')
        def bina(l,r):
            if l<=r:
                mid = (l+r)//2
                self.ind = min(self.ind,nums[mid])
                bina(l,mid-1) 
                bina(mid+1,r)
        bina(i,j)
        return self.ind