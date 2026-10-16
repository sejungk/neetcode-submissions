# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        curr = head

        while curr:
            nodes.append(curr)
            curr = curr.next

        n = len(nodes)
        if n <= 2:
            return 

        curr = head
        right = n-1
        left = 1

        for i in range(n-1):
            if i % 2 == 1:
                curr.next = nodes[left]
                left += 1
            else:
                curr.next = nodes[right]
                right -= 1

            curr = curr.next

        curr.next = None
