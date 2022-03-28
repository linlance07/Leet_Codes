# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        D = defaultdict(list)
        def dfs(temp,lev):
            if temp==None:
                return
            D[lev].append(temp.val)
            dfs(temp.left,lev+1)
            dfs(temp.right,lev+1)            
        dfs(root,0)
        return list(D.values())[::-1]