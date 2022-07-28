class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        Q = [('(',1,0)]
        ans = []
        while Q:
            b,l,r = Q.pop(0)
            if l>n or r>n or r>l:
                continue            
            if l==n and r==n:
                ans.append(b)
                continue
            Q.append((b+'(',l+1,r))
            Q.append((b+')',l,r+1))
        return ans
            
            