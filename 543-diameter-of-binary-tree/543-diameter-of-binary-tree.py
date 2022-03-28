# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_val = 0
        def dia(temp):
            if temp==None:
                return 0
            left = dia(temp.left)
            right = dia(temp.right)
            self.max_val = max(self.max_val,left+right)
            return 1 + max(left,right)
        dia(root)
        return self.max_val