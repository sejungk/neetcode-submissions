class Node:
    def __init__(self, val = None, key = None, next = None, prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity   
        self.key_to_node = {}  
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_front_node(self, node):
        next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node

    def _remove_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
            
    def get(self, key: int) -> int:
        if key not in self.key_to_node:
            return -1
        
        node = self.key_to_node[key]

        if node != self.head.next:
            self._remove_node(node)
            self._add_front_node(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            self._remove_node(node)
            node.val = value
            self._add_front_node(node)
        else:
            node = Node(value, key)
            self.key_to_node[key] = node
            self._add_front_node(node)  
            
            self.capacity -= 1
            if self.capacity < 0:
                node = self.tail.prev
                self._remove_node(node)
                del self.key_to_node[node.key]
                self.capacity += 1




        
