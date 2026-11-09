# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(None)
        dummy.next = head
        prev = dummy
        curr = dummy

        for i in range(n + 1):
            curr = curr.next

        while curr:
            prev = prev.next
            curr = curr.next
        
        next = prev.next.next
        prev.next = next
        
        return dummy.next