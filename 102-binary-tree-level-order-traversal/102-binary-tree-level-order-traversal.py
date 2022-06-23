# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        D = {}
        def levelorder(temp,lev):
            if temp==None:
                return
            if lev not in D:
                D[lev] = []
            D[lev].append(temp.val)
            levelorder(temp.left,lev+1)
            levelorder(temp.right,lev+1)  
        levelorder(root,0)
        return [x for x in D.values()]
            
            
        