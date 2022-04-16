# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.D = defaultdict(lambda:False)
        def put(temp,val):
            if temp:
                temp.val = val
                self.D[temp.val] = True
                put(temp.left,2*val+1)
                put(temp.right,2*val+2)
        put(root,0)        
    def find(self, target: int) -> bool:
        return self.D[target]


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)