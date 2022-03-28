# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, pre, ino):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        d=defaultdict(lambda:0)
        for i in range(len(ino)):
            d[ino[i]]=i
        global g
        g=0
        def rec(l,r):
            global g
            if l>r:
                return None
            root=TreeNode(pre[g])
            k=g
            g+=1
            
            if l==r:
                return root
            root.left=rec(l,d[pre[k]]-1)
            root.right=rec(d[pre[k]]+1,r)
            return root
        return rec(0,len(pre)-1)
        