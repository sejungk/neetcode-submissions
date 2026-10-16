# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        def order_list(front, back):
            if not back:
                return front
            
            front = order_list(front, back.next)

            if not front:
                return None
                
            if front == back or front.next == back:
                back.next = None
                return None
            else:
                next_front = front.next
                front.next = back
                back.next = next_front
                return next_front


        order_list(head, head.next)