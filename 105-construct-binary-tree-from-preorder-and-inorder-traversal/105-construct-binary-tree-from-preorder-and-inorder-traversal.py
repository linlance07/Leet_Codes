# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        D = {}
        for i in range(len(inorder)):
            D[inorder[i]] = i
        global ind
        ind = 0
        def ins(l,r):
            global ind
            if l>r:
                return None
            root = TreeNode(preorder[ind])
            g = ind
            ind += 1
            if l==r:
                return root
            root.left = ins(l,D[preorder[g]]-1)
            root.right = ins(D[preorder[g]]+1,r)
            return root
        return ins(0,len(inorder)-1)