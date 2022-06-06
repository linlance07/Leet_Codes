# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = b = 0
        temp =  headA
        temp2 = headB
        while temp:
            a+=1
            temp = temp.next
        while temp2:
            b+=1
            temp2 = temp2.next
        c = abs(a-b)
        temp = headA
        temp2 = headB
        for _ in range(c):
            if a>b:
                temp = temp.next
            else:
                temp2 = temp2.next
        while temp!=temp2:
            temp = temp.next
            temp2 = temp2.next
        if temp or temp2:
            return temp
        return None
            
                