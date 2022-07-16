class NumArray:

    def __init__(self, nums: List[int]):
        self.arr = nums
        self.SEG = [0] * 4*(len(nums))
        def build(ind,l,r):
            if l==r:
                self.SEG[ind] = nums[l]
                return
            mid = (l+r)//2
            build(2*ind+1,l,mid)
            build(2*ind+2,mid+1,r)
            self.SEG[ind] = self.SEG[2*ind+1] + self.SEG[2*ind+2]
        build(0,0,len(nums)-1) #index,left,right
        #print(self.SEG)
        
    def update(self, index: int, val: int) -> None:
        def upd(ind,l,r,index,val):
            if l==r and l==index:
                self.SEG[ind] = val
                return 
            mid = (l+r)//2
            if index<=mid:
                upd(ind*2+1,l,mid,index,val)
            else:
                upd(ind*2+2,mid+1,r,index,val)
            self.SEG[ind] = self.SEG[2*ind+1] + self.SEG[2*ind+2]
        upd(0,0,len(self.arr)-1,index,val)
        #print(self.SEG)

    def sumRange(self, left: int, right: int) -> int:
        def Range(ind,l,r,left,right):
            if left<=l<=r<=right:
                return self.SEG[ind]
            elif right<l or left>r:
                return 0
            else:
                mid = (l+r)//2
                return Range(2*ind+1,l,mid,left,right) + Range(2*ind+2,mid+1,r,left,right) 
        return Range(0,0,len(self.arr)-1,left,right)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)