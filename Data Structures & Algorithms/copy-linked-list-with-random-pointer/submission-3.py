"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
            
        curr = head

        while curr:
            next = curr.next
            curr.next = Node(curr.val)
            curr.next.next = next
            curr = next

        curr = head
        while curr:
            clone = curr.next
            clone.random = curr.random.next if curr.random else None
            curr = clone.next

        clone_head = head.next
        curr = head
        while curr:
            clone = curr.next
            curr.next = clone.next
            curr = curr.next
            clone.next = curr.next if curr else None
        
        return clone_head
            