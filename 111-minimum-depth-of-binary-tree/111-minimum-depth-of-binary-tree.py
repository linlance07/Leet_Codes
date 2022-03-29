# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(temp):
            if temp==None:
                return 0
            if temp.left and temp.right:
                return 1 + min(dfs(temp.left),dfs(temp.right))
            elif temp.left:
                return 1 + dfs(temp.left)
            elif temp.right:
                return 1 + dfs(temp.right)
            else:
                return 1
        return dfs(root)
                    
                    