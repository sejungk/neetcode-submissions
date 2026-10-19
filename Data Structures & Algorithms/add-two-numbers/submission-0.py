# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = ""
        num2 = ""

        curr = l1
        while curr:
            num1 = str(curr.val) + num1
            curr = curr.next

        curr = l2
        while curr:
            num2 = str(curr.val) + num2
            curr = curr.next

        total_sum = str(int(num1) + int(num2))
        i = 0
        dummy_head = ListNode(None)
        curr = dummy_head
        for digit in reversed(total_sum):
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy_head.next


        