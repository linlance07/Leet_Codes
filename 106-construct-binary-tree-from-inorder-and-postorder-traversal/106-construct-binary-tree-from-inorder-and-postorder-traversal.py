# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        D = {}
        for i in range(len(inorder)):
            D[inorder[i]] = i
        global ind
        ind = len(inorder)-1
        def ins(l,r):
            global ind
            if l>r:
                return None
            root = TreeNode(postorder[ind])
            g = ind
            ind -= 1
            if l==r:
                return root
            root.right = ins(D[postorder[g]]+1,r)
            root.left = ins(l,D[postorder[g]]-1)
            return root
        return ins(0,len(inorder)-1)