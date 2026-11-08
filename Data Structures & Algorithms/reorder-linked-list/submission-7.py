# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        #find divide
        while fast and fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        start = slow.next
        slow.next = None
     
        #reverse
        prev = None
        curr = start
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        dummy = ListNode(None)
        curr = dummy
        node1 = head
        node2 = prev
        while node1 and node2:
            curr.next = node1
            curr = curr.next
            node1 = node1.next
            
            curr.next = node2
            curr = curr.next
            node2 = node2.next

        if node1:
            curr.next = node1
            
        head = dummy.next
