# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
            
        def dfs(node):
            if not node:
                return

            if val < node.val:
                if node.left == None:
                    node.left = TreeNode(val)
                    return 
                dfs(node.left)
            else:
                if node.right == None:
                    node.right = TreeNode(val)
                    return 
                dfs(node.right)
        dfs(root)
        return root