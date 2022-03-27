# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        if not temp or not temp.next:
            return head
        HEAD = prev = ListNode()
        while temp and temp.next:
            nextt = temp.next.next
            sec = temp.next
            sec.next = temp
            temp.next = nextt
            prev.next = sec
            prev = temp
            temp = nextt
        return HEAD.next