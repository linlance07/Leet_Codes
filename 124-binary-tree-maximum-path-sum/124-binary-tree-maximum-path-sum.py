# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -float('inf')
        def dfs(temp):
            if not temp:
                return 0
            lg = max(dfs(temp.left),0)
            rg = max(dfs(temp.right),0)
            curr = temp.val + lg + rg
            self.ans = max(self.ans,curr)
            return temp.val + max(lg,rg)
        dfs(root)
        return self.ans