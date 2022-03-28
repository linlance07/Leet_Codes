# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        left = 0
        right = len(nums)-1
        root = None
        def ins(left,right):
            if left<=right:
                mid = (left + right)//2
                root = TreeNode(nums[mid])
                root.left = ins(left,mid-1)
                root.right = ins(mid+1,right)
                return root
        return ins(left,right)