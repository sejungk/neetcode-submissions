# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def is_ancestor(parent, node):
            if parent == None:
                return False

            if node == parent:
                return True
            
            return is_ancestor(parent.left, node) or is_ancestor(parent.right, node)
        
        res = None
        def dfs(node):
            nonlocal res
            if node == None:
                return
            
            if is_ancestor(node, p) and is_ancestor(node, q):
                res = node
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return res
