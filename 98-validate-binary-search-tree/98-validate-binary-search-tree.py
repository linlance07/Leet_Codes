# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        def inorder(temp):
            nonlocal ans
            if temp:
                inorder(temp.left)
                ans.append(temp.val)
                inorder(temp.right)
        inorder(root)
        return ans==sorted(set(ans))    
        # def valid(temp,mini,maxi):
        #     if temp==None:
        #         return True
        #     if temp.val<=mini or temp.val>=maxi:
        #         return False
        #     return valid(temp.left,mini,temp.val) and valid(temp.right,temp.val,maxi)
        # return valid(root,-math.inf,math.inf)