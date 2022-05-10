class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1,10))
        global ans
        ans = []
        def combi(c,s,path):
            if c==k:
                if s==n:
                    ans.append(path[1:])
                return
            if s>n:
                return
            for _ in range(path[-1]+1,10):
                combi(c+1,s+_,path+[_])
            
            
        combi(0,0,[0]) #count,sum,path
        return ans