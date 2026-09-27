# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def is_same_tree(node1, node2):
            if node1 == None and node2 == None:
                return True

            if node1 == None or node2 == None:
                return False

            if node1.val != node2.val:
                return False

            left_branch = is_same_tree(node1.left, node2.left)
            right_branch = is_same_tree(node1.right, node2.right)

            return left_branch and right_branch


        def dfs(node1, node2):
            if node1 == None or node2 == None:
                return False

            if node1.val == node2.val:
                if is_same_tree(node1, node2):
                    return True
            
            return dfs(node1.left, node2) or dfs(node1.right, node2)

            
        if root == None:
            return True
        
        return dfs(root, subRoot)
