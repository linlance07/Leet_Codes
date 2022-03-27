# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not(head):
            return None
        temp = head
        n = 0
        while temp:
            n+=1
            temp = temp.next
        k = k%n
        ind = n-k
        if k==0 or n==1 or ind==n:
            return head
        i = 0
        temp = head
        prev = None
        while i<ind:
            i+=1
            prev = temp
            temp = temp.next
        head2 = temp
        if prev:
            prev.next = None
        while temp.next:
            temp = temp.next
        temp.next = head
        return head2