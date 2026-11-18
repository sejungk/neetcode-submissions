# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        curr1 = l1
        curr2 = l2
        
        dummy = ListNode(None)
        curr = dummy
        while curr1 or curr2 or carry:
            num1 = curr1.val if curr1 else 0
            num2 = curr2.val if curr2 else 0

            total = num1 + num2 + carry
            curr.next = ListNode(total % 10)
            curr = curr.next

            carry = total // 10

            if curr1:
                curr1 = curr1.next
            
            if curr2:
                curr2 = curr2.next

        return dummy.next
            
