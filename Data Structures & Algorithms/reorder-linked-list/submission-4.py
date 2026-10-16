# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Empty or one-node lists are already reordered.
        if not head or not head.next:
            return

        def reorder_from_ends(front_node, back_node):
            # Recurse to the end before changing any links.
            if not back_node:
                return front_node
            
            # As calls return, front_node advances from the beginning.
            front_node = reorder_from_ends(front_node, back_node.next)
            
            # A deeper call found the middle or passed it
            if not front_node:
                return None

            # Stop when the front and back meet or become adjacent (even/odd length lists)
            if front_node == back_node or front_node.next == back_node:
                back_node.next = None
                return None

            #save next ref, move front pointer to back node, back node points to next front
            next_front_node = front_node.next
            front_node.next = back_node
            back_node.next = next_front_node

            # Pass the next unprocessed front node to the previous call.
            return next_front_node

        reorder_from_ends(head, head.next)