# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same(node1, node2):
            if node1 == None or node2 == None:
                return node1 == node2
            
            return (
                node1.val == node2.val and
                is_same(node1.left, node2.left) and 
                is_same(node1.right, node2.right)
            )

        def dfs(node):
            if not node:
                return False
            
            return (
                is_same(node, subRoot) or 
                dfs(node.left) or 
                dfs(node.right)
            )

        return dfs(root)