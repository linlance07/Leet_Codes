class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        i = 0
        j = len(nums)-1
        self.ind = False
        def bina(l,r):
            if l<=r:
                mid = (l+r)//2
                if nums[mid]==target:
                    self.ind = True
                bina(l,mid-1) 
                bina(mid+1,r)
        bina(i,j)
        return self.ind