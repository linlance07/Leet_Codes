# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        arr = []
        while temp:
            while arr and arr[-1]<temp.val:
                arr.pop()
            arr.append(temp.val)
            temp = temp.next
        dummy = head = ListNode()
        for i in arr:
            dummy.next = ListNode(i)
            dummy = dummy.next
        return head.next
        
            