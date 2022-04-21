# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def inner(temp,tempy):
            if temp==None and tempy==None:
                return True
            if tempy==None or temp==None:
                return False
            if temp.val!=tempy.val:
                return False
            return inner(temp.left,tempy.left) and inner(temp.right,tempy.right)
        def search(temp):
            if temp==None:
                return False
            if temp.val==subRoot.val and inner(temp,subRoot):
                return True
            return search(temp.left) or search(temp.right)
        return search(root)