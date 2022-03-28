# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr = []
        global s
        s = 0
        def dfs(temp,path):
            global s
            if temp==None:
                return
            if not temp.left and not temp.right:
                s += int(path+str(temp.val))
                return
            path += str(temp.val)
            dfs(temp.left,path)
            dfs(temp.right,path)
        dfs(root,"")
        return s
            