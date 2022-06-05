# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        Q = [root]
        ans = []
        while Q:
            n = len(Q)
            maxi = -float('inf')
            for _ in range(n):
                q = Q.pop(0)
                maxi = max(maxi,q.val)
                if q.left:
                    Q.append(q.left)
                if q.right:
                    Q.append(q.right)
            ans.append(maxi)
        return ans
                    
                