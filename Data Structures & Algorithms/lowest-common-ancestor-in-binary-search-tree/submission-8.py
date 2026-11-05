# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        stack = [root]
        while stack:
            node = stack.pop()

            if node.val > max(p.val, q.val):
                stack.append(node.left)
            elif node.val < min(p.val, q.val):
                stack.append(node.right)
            else:
                return node