# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def LCA(temp):
            if not temp:
                return None
            if temp==p or temp==q:
                return temp
            left = LCA(temp.left)
            right = LCA(temp.right)
            if left and right:
                return temp
            if left:
                return left
            if right:
                return right
        return LCA(root)