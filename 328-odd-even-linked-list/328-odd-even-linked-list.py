# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        O = odd = ListNode()
        E = even = ListNode()
        temp = head
        ind = 0
        while temp:
            if ind%2:
                even.next = temp
                even = even.next
            else:
                odd.next = temp
                odd = odd.next
            temp = temp.next
            ind += 1
            print(odd.val,even.val)
        #print(odd.val,E.next.val)
        odd.next = E.next
        even.next = None
        return O.next