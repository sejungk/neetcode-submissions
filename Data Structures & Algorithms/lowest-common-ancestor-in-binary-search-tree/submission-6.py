# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def contains(node, val):
            if node == None:
                return False
            
            return (
                node == val or
                contains(node.left, val) or 
                contains(node.right, val)
            )

        def dfs(node):
            if node == None:
                return 

            if node.left and contains(node.left, p) and contains(node.left, q):
                return dfs(node.left)
            
            elif node.right and contains(node.right, p) and contains(node.right, q):
                return dfs(node.right)
            else:
                return node

        return dfs(root)