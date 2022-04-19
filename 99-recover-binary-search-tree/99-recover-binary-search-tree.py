# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        global ino
        global inoval
        ino = []
        inoval = []
        def inord(temp):
            global ino
            if temp:
                inord(temp.left)
                ino.append(temp)
                inoval.append(temp.val)
                inord(temp.right)
        inord(root)
        sorty = sorted(inoval)
        for j in range(len(sorty)):
            ino[j].val = sorty[j]
                
        