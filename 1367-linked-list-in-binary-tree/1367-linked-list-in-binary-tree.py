class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(root,temp):
            if temp==None:
                return True
            if root==None:
                return False
            if root.val==temp.val and sub(root,temp):
                return True
            return dfs(root.left,temp) or dfs(root.right,temp)

        def sub(root,temp):
            if temp==None:
                return True
            if not root:
                return False
            if root.val!=temp.val:
                return False
            return sub(root.left,temp.next) or sub(root.right,temp.next)
                  
        return dfs(root,head)