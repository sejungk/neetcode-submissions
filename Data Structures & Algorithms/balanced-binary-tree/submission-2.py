# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def isBalanced(self, root: Optional[TreeNode]) -> bool:
    #     def dfs(node):
    #         if not node:
    #             return [True, 0]

    #         left_branch = dfs(node.left)
    #         right_branch = dfs(node.right)
    #         balanced = left_branch[0] and right_branch[0] and abs(left_branch[1] - right_branch[1]) <= 1

    #         return [balanced, 1 + max(left_branch[1], right_branch[1])]

    #     return dfs(root)[0]

   def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = []
        node = root
        last = None
        depths = {}

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    stack.pop()
                    left = depths.get(node.left, 0)
                    right = depths.get(node.right, 0)

                    if abs(left - right) > 1:
                        return False
                    
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        
        return True