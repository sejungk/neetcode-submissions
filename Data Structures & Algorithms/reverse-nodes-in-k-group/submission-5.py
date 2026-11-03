# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        group_prev = dummy

        def get_group_kth_end(curr):
            count = 0
            while curr and count < k:
                curr = curr.next 
                count += 1
            return curr

        while True:
            group_kth_end = get_group_kth_end(group_prev)
            if not group_kth_end:
                break
            group_next = group_kth_end.next

            # set prev to remaining list so it can be connected
            prev = group_kth_end.next
            # set curr to beginning of list
            curr = group_prev.next
            while curr != group_next:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            curr_group = group_prev.next
            group_prev.next = group_kth_end
            group_prev = curr_group

        return dummy.next
