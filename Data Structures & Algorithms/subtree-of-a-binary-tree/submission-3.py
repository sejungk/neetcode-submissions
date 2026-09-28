# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(node):
            if node == None:
                return "end"
            
            path = f".{node.val}." + dfs(node.left) + dfs(node.right)
            return path

        tree1 = dfs(root)
        tree2 = dfs(subRoot)

        return tree2 in tree1

