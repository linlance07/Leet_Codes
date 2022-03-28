# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        Q = []
        Q.append(root)
        ans = []
        while Q:
            n = len(Q)
            s = 0
            c = 0
            for _ in range(n):
                node = Q.pop(0)
                if node:
                    s += node.val
                    c += 1
                    Q.append(node.left)
                    Q.append(node.right)
            if c:
                ans.append(s/c)
        return ans
                    