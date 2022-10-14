# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        prev = nexts = None
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        nexts = slow.next
        if prev:
            prev.next = nexts
        else:
            return None
        return head
            