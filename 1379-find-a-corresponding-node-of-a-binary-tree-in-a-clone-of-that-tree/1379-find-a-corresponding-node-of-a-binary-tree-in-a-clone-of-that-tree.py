# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        ans = TreeNode()
        def search(temp,temp2):
            if temp and temp2:
                if temp==target:
                    ans.next = temp2
                search(temp.left,temp2.left)
                search(temp.right,temp2.right)
        search(original,cloned)    
        return ans.next