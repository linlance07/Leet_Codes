# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.max=0
        def rec(r):
            if not r:
                return 0
            lef=rec(r.left)
            rig=rec(r.right)
            self.max=max(self.max,lef+rig)
            h=1+max(lef,rig)
            return h
        rec(root)
        return self.max