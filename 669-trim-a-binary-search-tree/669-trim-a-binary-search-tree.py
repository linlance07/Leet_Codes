# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def trim(temp):
            if not temp:
                return None
            if temp.val<low:
                return trim(temp.right)
            if temp.val>high:
                return trim(temp.left)
            temp.left = trim(temp.left)
            temp.right = trim(temp.right)
            return temp      
        return trim(root)
            
            