# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        Q = []
        Q.append(root)
        ans = []
        while Q:
            n = len(Q)
            arr = []
            for _ in range(n):
                node = Q.pop(0)
                if node:
                    arr.append(node.val)
                    Q.append(node.left)
                    Q.append(node.right)
            if arr:
                ans.append(arr)
        return ans[::-1]