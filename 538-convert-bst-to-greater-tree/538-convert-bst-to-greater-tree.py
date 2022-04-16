# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        global ans
        ans = 0
        def dfs(temp):
            global ans
            if temp:
                dfs(temp.right)
                ans += temp.val
                temp.val = ans
                dfs(temp.left)
        dfs(root)
        return root