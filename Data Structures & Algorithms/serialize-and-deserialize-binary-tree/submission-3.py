# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "N"

        res = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                res.append("N")
            else:
                res.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        return ".".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        pre = data.split(".")
        if pre[0] == "N":
            return None
        
        i = 1
        root = TreeNode(int(pre[0]))
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if pre[i] != "N":
                node.left = TreeNode(int(pre[i]))
                queue.append(node.left)
            i += 1
            if pre[i] != "N":
                node.right = TreeNode(int(pre[i]))
                queue.append(node.right)
            i += 1
        return root

