# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def depth(temp):
            if temp==None:
                return 0 
            return 1+max(depth(temp.left),depth(temp.right))
        depth_val = depth(root)
        def deep(temp,lev):
            if temp==None:
                return 0
            if temp.left==None and temp.right==None and lev==depth_val:
                return temp.val
            return deep(temp.left,lev+1) + deep(temp.right,lev+1)   
        return deep(root,1)