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
        node_to_copy = {}

        curr = head
        while curr:
            copy = Node(curr.val)
            node_to_copy[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = node_to_copy[curr]
            if curr.next:
                copy.next = node_to_copy[curr.next]
            if curr.random:
                copy.random = node_to_copy[curr.random]
            curr = curr.next

        return node_to_copy[head]