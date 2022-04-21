# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        D = defaultdict(lambda:0)
        def dfs(temp):
            if temp.left==None and temp.right==None:
                D[temp.val] += 1
                return temp.val
            if temp.right and temp.left:
                temp.val += dfs(temp.left)
                temp.val += dfs(temp.right)
            elif temp.left:
                temp.val += dfs(temp.left)
            else:
                temp.val += dfs(temp.right)
            D[temp.val] += 1
            return temp.val
        dfs(root)
        arr = list(D.values())
        maxi = max(arr)
        ans = []
        for j in D:
            if D[j]==maxi:
                ans.append(j)
        return ans