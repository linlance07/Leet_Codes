# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def rec(root):
            if not root:
                return None
            root.left=rec(root.left)
            root.right=rec(root.right)
            if root.val==target:
                if not root.left and not root.right:
                    return None

            
            return root
        return rec(root)