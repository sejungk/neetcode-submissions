# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # def maxDepth(self, root: Optional[TreeNode]) -> int:
        
    #     def dfs(node):
    #         if not node:
    #             return 0

    #         max_count = 1 + max(dfs(node.left), dfs(node.right))
    #         return max_count

    #     return dfs(root)

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     if not root:
    #         return 0

    #     stack = [(root, 1)]
    #     max_count = 0

    #     while stack:
    #         node, depth = stack.pop()
    #         max_count = max(max_count, depth)

    #         if node.left:
    #             stack.append((node.left, depth + 1))
            
    #         if node.right:
    #             stack.append((node.right, depth + 1))


    #     return max_count

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        queue = deque()
        queue.append((root, 1))

        while queue:
            node, depth = queue.popleft()

            if node.left:
                queue.append((node.left, depth + 1))
            
            if node.right:
                queue.append((node.right, depth + 1))

        return depth
        