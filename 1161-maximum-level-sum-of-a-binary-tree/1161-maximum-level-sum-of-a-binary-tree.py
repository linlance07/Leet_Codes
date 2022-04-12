# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        D = defaultdict(lambda:0)
        def dfs(temp,lev):
            if temp==None:
                return
            D[lev] += temp.val
            dfs(temp.left,lev+1)
            dfs(temp.right,lev+1)
        dfs(root,1)
        ans = (None,-float('inf'))
        for i in D:
            if D[i]>ans[1]:
                ans = (i,D[i])
        return ans[0]