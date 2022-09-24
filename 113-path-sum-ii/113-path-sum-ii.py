# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(temp,path,s):
            if temp==None:
                return 
            s += temp.val
            if temp.left==None and temp.right==None:
                if s==targetSum:
                    ans.append(path+[temp.val])
                    return
            dfs(temp.left,path+[temp.val],s)
            dfs(temp.right,path+[temp.val],s)
        dfs(root,[],0)
        return ans