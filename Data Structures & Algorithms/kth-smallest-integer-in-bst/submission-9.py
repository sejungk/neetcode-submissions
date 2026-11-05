# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def count_nodes(node):
            if not node:
                return 0 
            
            return 1 + count_nodes(node.left) + count_nodes(node.right)

        count = count_nodes(root)

        def dfs(node):
            nonlocal k
            if node == None:
                return None
            
            res = dfs(node.left)
            if res is not None:
                return res

            k -= 1
            if k == 0:
                return node.val

            return dfs(node.right)
            
        return dfs(root)