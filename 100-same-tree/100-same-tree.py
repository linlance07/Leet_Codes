# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def same(l,r):
            if l==None and r==None:
                return True
            if l==None or r==None:
                return False
            if l.val!=r.val:
                return False
            return same(l.left,r.left) and same(l.right,r.right)            
        return same(p,q)