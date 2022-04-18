# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        s = set()
        def dfs(temp):
            if temp:
                dfs(temp.left)
                s.add(temp.val)
                dfs(temp.right)
        dfs(root)
        l = list(s)
        ll = sorted(l)
        if len(ll)<=1:
            return -1
        return ll[1]