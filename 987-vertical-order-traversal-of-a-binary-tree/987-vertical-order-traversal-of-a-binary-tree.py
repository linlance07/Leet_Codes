# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        D = defaultdict(list)
        def vert(temp,dis,l):
            if temp==None:
                return
            D[dis].append([l,temp.val])
            vert(temp.left,dis-1,l+1)
            vert(temp.right,dis+1,l+1)
        vert(root,0,0)
        arr = sorted(D)
        ans = []
        print(D,arr)
        res=[]
        for j in arr:
            ans=[]
            for i in sorted(D[j]):
                ans.append(i[1])
            res.append(ans)
        return res
            
            
            
            
        