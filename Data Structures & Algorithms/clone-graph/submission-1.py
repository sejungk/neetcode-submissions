"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        clone_map = {}

        def dfs(node):
            if not node:
                return None

            if node in clone_map:
                return clone_map[node]

            if node not in clone_map:
                clone_map[node] = clone = Node(node.val)
            
            clone = clone_map[node]
            
            for nei in node.neighbors:
                clone.neighbors.append(dfs(nei))
            
            return clone
        
        return dfs(node)