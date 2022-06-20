# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1==None:
            return l2
        if l2==None:
            return l1
        head3 = ListNode()
        temp3 = head3
        while l1 and l2:
            if l1.val<=l2.val:
                temp3.next = l1
                l1 = l1.next
            else:
                temp3.next = l2
                l2 = l2.next
            temp3 = temp3.next
        if l1:
            temp3.next = l1
        if l2:
            temp3.next = l2
        return head3.next
                    
                        