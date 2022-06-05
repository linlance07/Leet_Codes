# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        global prev
        prev = None
        def flat(temp):
            global prev
            if temp==None:
                return 
            flat(temp.right)
            flat(temp.left)
            temp.left = None
            temp.right = prev
            prev = temp
        flat(root)
        