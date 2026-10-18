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
        original_to_copy = {}
        dummy_head = Node(0)

        ori_curr = head
        new_curr = dummy_head
        while ori_curr:
            new_curr.next = Node(ori_curr.val)
            new_curr = new_curr.next
            original_to_copy[ori_curr] = new_curr
            ori_curr = ori_curr.next

        ori_curr = head
        new_curr = dummy_head.next
        while ori_curr:
            new_curr.random = original_to_copy.get(ori_curr.random)

            ori_curr = ori_curr.next
            new_curr = new_curr.next

        return dummy_head.next