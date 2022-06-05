# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        Q = [root]
        B = False
        lev = 1
        while lev<depth:
            n = len(Q)
            for _ in range(n):
                q = Q.pop(0)
                if lev==depth-1:
                    L = q.left
                    q.left = TreeNode(val)
                    q.left.left = L
                    R = q.right
                    q.right = TreeNode(val)
                    q.right.right = R
                    B = True
                else:
                    if q.left:
                        Q.append(q.left)
                    if q.right:
                        Q.append(q.right)
            lev += 1
            if B:
                break
        if not B:
            ROOT = TreeNode(val)
            ROOT.left = root
            return ROOT
        return root