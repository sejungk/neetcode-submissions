# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float("-inf")
        
        def max_sum(node):
            nonlocal best

            if node == None:
                return 0
            
            left_branch = max(0, max_sum(node.left))
            right_branch = max(0, max_sum(node.right))

            best = max(best, node.val + left_branch + right_branch)
            return node.val + max(left_branch, right_branch)
            
        max_sum(root)
        return best
