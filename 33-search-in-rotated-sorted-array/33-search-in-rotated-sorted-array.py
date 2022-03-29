class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums)-1
        self.ind = -1
        def bina(l,r):
            if l<=r:
                mid = (l+r)//2
                if nums[mid]==target:
                    self.ind = mid
                bina(l,mid-1) 
                bina(mid+1,r)
        bina(i,j)
        return self.ind