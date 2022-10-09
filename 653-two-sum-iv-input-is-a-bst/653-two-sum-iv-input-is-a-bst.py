# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        D = set()
        def find(temp):
            if temp==None:
                return False
            if k-temp.val in D:
                return True
            else:
                D.add(temp.val)
            return find(temp.left) or find(temp.right)
        #print(D)
        return find(root)