# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        order = []

        def dfs(node):
            if node == None:
                return

            dfs(node.left)
            order.append(node.val)
            dfs(node.right)
        
        dfs(root)
        return order == sorted(order) and len(set(order)) == len(order)