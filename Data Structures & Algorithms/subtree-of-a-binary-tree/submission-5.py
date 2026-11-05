# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False

        def is_same(node1, node2):
            if node1 == None or node2 == None:
                return False
            
            if node1.val != node2.val:
                return False
            
            if node1.left or node2.left:
                if not is_same(node1.left, node2.left):
                    return False
            
            if node2.right or node1.right:
                if not is_same(node1.right, node2.right):
                    return False
            
            return True
            

        def dfs(node1, node2):
            if node1.val == node2.val:
                if is_same(node1, node2):
                    return True
            
            if node1.right:
                if dfs(node1.right, node2):
                    return True
                
            if node1.left:
                if dfs(node1.left, node2):
                    return True
            
            return False


        return dfs(root, subRoot)