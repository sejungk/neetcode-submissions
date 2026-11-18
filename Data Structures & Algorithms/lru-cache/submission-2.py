class Node:
    def __init__(self, val = None, key = None, next = None, prev = None):
        self.val = val
        self.key = key
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_node = defaultdict(str)
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_recently_used(self, node):
        if node.next and node.prev:
            #remove
            node.prev.next = node.next
            node.next.prev = node.prev

        # add to front
        new_next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = new_next
        new_next.prev = node

        self.key_to_node[node.key] = node

    def _remove_least_recently_used(self):
        node = self.tail.prev
        prev_node = node.prev
        node.prev.next = self.tail
        self.tail.prev = prev_node

        del self.key_to_node[node.key]

    def get(self, key: int) -> int:
        if key in self.key_to_node:
            node = self.key_to_node[key]            
            self._add_recently_used(node)

            return node.val

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.val = value

            self._add_recently_used(node)
        else:
            node = Node(value, key)
            self._add_recently_used(node)

            if self.capacity < len(self.key_to_node):
                self._remove_least_recently_used()

           
        
