# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0

        dummy_head = ListNode(None)
        curr1 = l1
        curr2 = l2
        curr3 = dummy_head

        while curr1 or curr2 or carry:
            num1 = curr1.val if curr1 else 0
            num2 = curr2.val if curr2 else 0

            curr_sum = num1 + num2 + carry

            carry = curr_sum // 10
            curr_sum = curr_sum % 10
            
            curr3.next = ListNode(curr_sum)
            curr3 = curr3.next

            if curr1:
                curr1 = curr1.next
            
            if curr2:
                curr2 = curr2.next

        return dummy_head.next