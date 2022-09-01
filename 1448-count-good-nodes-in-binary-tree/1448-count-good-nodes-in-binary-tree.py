# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def dfs(temp,maxi):
            nonlocal ans
            if not temp:
                return
            if temp.val>=maxi:
                ans += 1
            dfs(temp.left,max(maxi,temp.val))
            dfs(temp.right,max(maxi,temp.val))
        dfs(root,root.val)
        return ans