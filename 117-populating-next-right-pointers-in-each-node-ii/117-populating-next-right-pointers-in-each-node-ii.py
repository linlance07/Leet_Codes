"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        Q = [root]
        while Q:
            n = len(Q)
            res = []
            arr = []
            for j in range(n):
                q = Q.pop(0)
                if q and q.left:
                    res.append(q.left)
                    arr.append(q.left.val)
                if q and q.right:
                    res.append(q.right)
                    arr.append(q.right.val)
            for k in range(len(res)-1):
                res[k].next = res[k+1]
            Q = res        
        return root
        
        