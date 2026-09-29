# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         order = []

#         def dfs(node):
#             if node == None:
#                 return

#             dfs(node.left)
#             order.append(node.val)
#             dfs(node.right)
        
#         dfs(root)
#         return order == sorted(order) and len(set(order)) == len(order)

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if node == None:
                return True

            if not low < node.val < high:
                return False
            
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root, float("-inf"), float("inf"))