class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        lower = min(p.val, q.val)
        greater = max(p.val, q.val)

        while root:
            if root.val >= lower and root.val <= greater:
                return root
            elif root.val > lower and root.val > greater:
                root = root.left
            else:
                root = root.right