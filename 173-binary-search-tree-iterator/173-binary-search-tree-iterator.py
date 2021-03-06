# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.inorder = []
        def inorder(root):
            if root:
                inorder(root.left)
                self.inorder.append(root.val)
                inorder(root.right)
        inorder(root)
        
    def next(self) -> int:
        return self.inorder.pop(0)

    def hasNext(self) -> bool:
        if self.inorder:
            return True
        return False


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()