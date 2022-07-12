# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        R = L = None
        temp = head
        temp2 = head
        for i in range(left-1):
            L = temp
            temp = temp.next
        for i in range(right-1):
            temp2 = temp2.next
            R = temp2.next
        nxt = None
        c = right - left + 1
        if L:
            L.next = temp2
        else:
            head = temp2
        while c:
            nxt = temp.next
            temp.next = R
            R = temp
            temp = nxt
            c -= 1
        return head
        
        
        
        
            