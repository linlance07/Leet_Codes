# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        count = 0
        temp = head
        prev = nxt = None
        while temp:
            count += 1
            nxt = temp.next
            temp.next = prev
            prev = temp
            head = prev
            temp = nxt
        ans = [0 for _ in range(count)]
        temp = head
        stack = []
        while temp:
            count -= 1
            while stack and stack[-1]<=temp.val:
                stack.pop()
            if stack:
                ans[count] = stack[-1]
            stack.append(temp.val)
            #print(ans,count,temp.val,stack)
            temp = temp.next
            
        return ans
        