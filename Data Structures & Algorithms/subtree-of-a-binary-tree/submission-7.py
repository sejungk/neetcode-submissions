# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        tree1 = []
        tree2 = []

        def serialize(node, tree):
            if not node:
                tree.append("#")
                return

            tree.append(str(node.val))
            serialize(node.left, tree)
            serialize(node.right, tree)

        serialize(root, tree1)
        serialize(subRoot, tree2)

        return ",".join(tree2) in ",".join(tree1)