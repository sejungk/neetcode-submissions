# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = ""

        def dfs(node, parent_val, pos):
            nonlocal res
            if node == None:
                res += f".N"
                return
            
            res += f".{node.val}"
            dfs(node.left, node.val, "left")
            dfs(node.right, node.val, "right")

        dfs(root, None, None)
        return res
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data[1:].split(".")
        i = 0

        def dfs():
            nonlocal i

            val = nodes[i]
            i += 1

            if val == "N":
                return None
            
            node = TreeNode(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
            
        return dfs()
        


