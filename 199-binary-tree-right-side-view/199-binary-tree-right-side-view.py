# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        D = {}
        ans = []
        def dfs(temp,lev):
            if temp==None:
                return
            if lev not in D:
                D[lev] = []
            D[lev].append(temp.val)
            dfs(temp.right,lev+1)
            dfs(temp.left,lev+1)
            return
        dfs(root,0)
        A = list(D.values())
        print(D)
        for i in A:
            ans.append(i[0])
        return ans