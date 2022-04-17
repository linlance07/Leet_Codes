# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        global new_root,Root
        new_root = Root = TreeNode()
        def inord(temp):
            global Root,new_root
            if temp:
                inord(temp.left)
                Root.right = TreeNode(temp.val)
                Root = Root.right
                inord(temp.right)
        inord(root)
        return new_root.right