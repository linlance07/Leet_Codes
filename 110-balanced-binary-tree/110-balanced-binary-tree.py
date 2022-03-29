# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def rec(r):
            if not r:
                return 0
            lef=rec(r.left)
            rig=rec(r.right)
            if abs(lef-rig)>1 or lef==-1 or rig==-1:
                return -1
            return 1+max(lef,rig)
        return rec(root)!=-1
        