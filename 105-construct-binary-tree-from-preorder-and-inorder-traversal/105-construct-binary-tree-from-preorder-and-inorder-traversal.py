# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        D = defaultdict(int)
        for i in range(len(inorder)):
            D[inorder[i]] = i
        ind = 0
        def dfs(l,r):
            nonlocal ind
            if l>r:
                return
            root = TreeNode(preorder[ind])
            g = ind
            ind += 1
            root.left = dfs(l,D[preorder[g]]-1)
            root.right = dfs(D[preorder[g]]+1,r)
            return root
        return dfs(0,len(inorder)-1)