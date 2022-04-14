# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def search(temp):
            if temp==None:
                return None
            if temp.val==val:
                return temp
            elif val<temp.val:
                return search(temp.left)
            else:
                return search(temp.right)     
        return search(root)