# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        def ino(r):
            if not r or not r.left:
                return r
            else:
                return ino(r.left)
        def dell(r,v):
            if not r:
                return None
            if v>r.val:
                r.right=dell(r.right,v)
            elif v<r.val:
                r.left=dell(r.left,v)
            else:
                if r.right==None:
                    t=r.left
                    r=None
                    return t
                if r.left==None:
                    t=r.right
                    r=None
                    return t
                t=ino(r.right)
                r.val=t.val
                r.right=dell(r.right,r.val)
            return r
        return dell(root,key)
                
                    
                
                