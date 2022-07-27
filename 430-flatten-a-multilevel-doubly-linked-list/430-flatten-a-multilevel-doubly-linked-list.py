"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new = head2 = Node()
        temp = head
        def flat(temp):
            nonlocal new
            if temp:
                new.next = Node(temp.val)
                new.next.prev  = new
                new = new.next
                flat(temp.child)
                flat(temp.next)
        flat(temp)
        head3 = head2.next
        if head3:
            head3.prev = None
        return head3