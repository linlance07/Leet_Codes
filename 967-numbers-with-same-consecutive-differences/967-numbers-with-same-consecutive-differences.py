class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = set()
        def dfs(i,lvl,path):
            nonlocal ans
            if i<0 or i>=10:
                return
            if lvl==n:
                ans.add(int(path))
                return 
            dfs(i+k,lvl+1,path+str(i+k))
            dfs(i-k,lvl+1,path+str(i-k))
        for i in range(1,10):
            dfs(i,1,str(i))
        return list(ans)
            