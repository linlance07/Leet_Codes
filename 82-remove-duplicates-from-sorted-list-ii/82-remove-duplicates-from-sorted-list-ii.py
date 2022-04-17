# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        D = {}
        temp = head
        while temp:
            D[temp.val] = D.get(temp.val,0)+1
            temp = temp.next
        temp = head
        prev = None
        while temp:
            if D[temp.val]>1:
                if temp==head:
                    head = head.next
                    temp = head
                else:
                    prev.next = temp.next
                    temp = temp.next
            else:
                prev = temp
                temp = temp.next  
        return head