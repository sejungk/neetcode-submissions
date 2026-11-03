# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            curr = node

            for i in range(k):
                next = curr.next
                curr.next = prev                                                                          
                prev = curr
                curr = next

            return prev

        dummy_head = ListNode()
        dummy_head.next = head
        prev = dummy_head
        start = head
        while start:
            count = 0
            end = start

            while end and count < (k - 1):
                end = end.next
                count += 1
            
            # finshed reversing
            if end == None:
                break

            # reverse and connect    
            remaining = end.next       
            prev.next = reverse(start)
            start.next = remaining    

            prev = start
            start = remaining
        return dummy_head.next