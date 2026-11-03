# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        def get_kth(curr):
            count = 0
            while curr and count < k:
                curr = curr.next 
                count += 1
            return curr

        while True:
            kth = get_kth(group_prev)
            if not kth:
                break
            group_next = kth.next

            prev = kth.next
            curr = group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = group_prev.next
            group_prev.next = kth
            group_prev = temp

        return dummy.next
