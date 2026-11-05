# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
            
        queue = deque([(p, q)])
        while queue:
            node1, node2 = queue.popleft()
            if node1 == None or node2 == None:
                return False

            if node1.val != node2.val:
                return False

            if node1.left or node2.left:
                queue.append((node1.left, node2.left))
            
            if node1.right or node2.right:
                queue.append((node1.right, node2.right))
            
        return True