# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, high, low):
            if node == None:
                return True

            if node.val >= high or node.val <= low:
                return False

            if node.left:
                if not dfs(node.left, node.val, low):
                    return False
            
            if node.right:
                if not dfs(node.right, high, node.val):
                    return False
            
            return True

        return dfs(root, float("inf"), -float("inf"))