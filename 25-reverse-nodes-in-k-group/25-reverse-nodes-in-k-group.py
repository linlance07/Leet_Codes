# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        global HEAD
        HEAD = None
        def rev(prev,temp,c):
            global HEAD
            if c:
                if temp:
                    rev(temp,temp.next,c-1)
                    temp.next = prev
            else:
                HEAD = prev
            return HEAD
        temp = head
        prev = None
        i = 1
        n = 0
        new_head = dummy = ListNode()
        while temp:
            n += 1
            temp = temp.next
        temp = head
        while i<=n-k+1:
            j = 1
            curr = temp
            while j<k:
                curr = curr.next
                j+=1
            nexts = curr.next
            i+=k
            dummy.next = rev(prev,temp,k)
            ptr = dummy.next
            while ptr.next:
                ptr = ptr.next
            dummy = ptr
            temp = nexts
        if temp:
            dummy.next = temp
        return new_head.next