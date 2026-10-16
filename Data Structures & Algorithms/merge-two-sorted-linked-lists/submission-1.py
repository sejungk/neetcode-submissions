# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        prev = dummy_head

        curr1 = list1
        curr2 = list2

        while curr2 and curr1:
            next = curr1.next

            if curr1.val < curr2.val:
                prev.next = curr1
                prev = curr1
                curr1 = curr1.next
            else:
                prev.next = curr2
                prev = curr2
                curr2 = curr2.next
            
        if curr1:
            prev.next = curr1
        
        if curr2:
            prev.next = curr2

        return dummy_head.next

