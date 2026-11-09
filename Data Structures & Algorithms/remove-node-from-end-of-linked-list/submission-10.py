# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []

        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        
        if len(nodes) == 1:
            return None

        if n == 1:
            nodes[n-3].next = None
            return head
        
        if n == len(nodes):
            head.next = None
            return nodes[1]

        prev = nodes[len(nodes) - (n + 1)]
        next_node = nodes[len(nodes) - (n - 1)]
        prev.next = next_node
        return head
        