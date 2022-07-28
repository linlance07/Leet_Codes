class Fenwick:
    def __init__(self,n):
        self.fen = [0]*(n+1)
    
    def update(self,ind,delta):
        while ind<len(self.fen):
            self.fen[ind] += delta
            ind += (ind&-ind)     
        
    def query(self,ind):
        res = 0
        while ind>0:
            res += self.fen[ind]
            ind -= (ind&-ind)
        return res


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        F = Fenwick(len(nums))
        ans = []
        arr = sorted(set(nums))
        D = defaultdict(int)
        for i,j in enumerate(arr):
            D[j] = i
        I = []
        for k in range(len(nums)):
            I.append(D[nums[k]])
        for l in range(len(I)-1,-1,-1):
            a = F.query(I[l])
            ans.append(a)
            F.update(I[l]+1,1)
        return ans[::-1]
            
        
        
        