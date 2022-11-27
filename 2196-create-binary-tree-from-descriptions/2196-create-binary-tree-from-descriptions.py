# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        parent = set()
        child = set()
        D = defaultdict(lambda:[None,None])
        for i,j,k in descriptions:
            if k:
                D[i][0] = j
            else:
                D[i][1] = j
            parent.add(i)
            child.add(j)
        R = parent - child
        root = TreeNode(R.pop())
        def create(temp):
            if D[temp.val]!=[None,None]:
                if D[temp.val][0]:
                    temp.left = TreeNode(D[temp.val][0])
                    create(temp.left)
                if D[temp.val][1]:
                    temp.right = TreeNode(D[temp.val][1])
                    create(temp.right)                
        create(root)
        return root
        
            