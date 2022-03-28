# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        arr = []
        def dfs(temp,path):
            if temp==None:
                return
            if not temp.left and not temp.right:
                arr.append(path+str(temp.val))
                return
            path += str(temp.val)
            dfs(temp.left,path)
            dfs(temp.right,path)
        dfs(root,"")
        s = 0
        for i in arr:
            s += int(i)
        return s
            