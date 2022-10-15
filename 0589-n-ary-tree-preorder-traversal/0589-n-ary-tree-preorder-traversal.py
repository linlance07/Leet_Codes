"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        def dfs(temp,ans):
            if temp==None:
                return ans
            ans.append(temp.val)
            for i in temp.children:
                dfs(i,ans)
            return ans    
        res = []
        return dfs(root,res)
        