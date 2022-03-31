"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        H = new_head = Node(0)
        temp = head
        D = {None:None}
        while temp:
            D[temp] = Node(temp.val)
            temp = temp.next
        temp = head
        while temp:
            node = D[temp]
            node.next = D[temp.next]
            node.random = D[temp.random]
            temp = temp.next
        return D[head]