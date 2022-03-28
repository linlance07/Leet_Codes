# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        global s
        s = ""
        def dfs(temp,path):
            global s
            if temp==None:
                return
            if temp.left==None and temp.right==None:
                if s=="":
                    s = (chr(temp.val+97)+path)
                else:
                    if (chr(temp.val+97)+path)<s:
                        s = (chr(temp.val+97)+path)
                return
            path = chr(temp.val+97) + path
            dfs(temp.left,path)
            dfs(temp.right,path)
        dfs(root,"")
        return s