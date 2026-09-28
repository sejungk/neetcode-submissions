# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        def assign_parent(curr, prev):
            if curr == None:
                return 
            curr.parent = prev
            assign_parent(curr.left, curr)
            assign_parent(curr.right, curr)
        
        assign_parent(root, None)

        seen = set()
        while p:
            seen.add(p)
            p = p.parent
        
        while q:
            if q in seen:
                return q
            q = q.parent
       
        
        return root