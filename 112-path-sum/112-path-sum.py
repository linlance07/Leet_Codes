# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return 0
        def search(temp,s):
            if temp==None:
                return False
            s-=temp.val
            if temp.left==None and temp.right==None:
                if s==0:
                    return True
            return search(temp.left,s) or search(temp.right,s)           
        return search(root,targetSum)