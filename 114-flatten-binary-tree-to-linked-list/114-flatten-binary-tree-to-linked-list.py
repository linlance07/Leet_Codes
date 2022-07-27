# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        prev = None
        def flat(temp):
            nonlocal prev
            if temp:
                flat(temp.right)
                flat(temp.left)
                temp.right = prev
                temp.left = None
                prev = temp
            
        flat(root)
        