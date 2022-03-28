# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def inord(temp):
            if temp and temp.left:
                return inord(temp.left)
            return temp
        def delete(temp,key):
            if temp==None:
                return None
            if key<temp.val:
                temp.left = delete(temp.left,key)
            elif key>temp.val:
                temp.right = delete(temp.right,key)
            else:
                if not temp.left:
                    return temp.right
                if not temp.right:
                    return temp.left
                inord_success =  inord(temp.right)
                temp.val = inord_success.val
                temp.right = delete(temp.right,inord_success.val)
            return temp  
        return delete(root,key)