
class LRUCache:

    class Node:
        def __init__(self, key: int, value: int, prev=None, next=None):
            self.key = key
            self.value = value
            self.prev = prev
            self.next = next

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = self.Node(0, 0)
        self.tail = self.Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """
        Return the value corresponding to the key if it exists,
        otherwise return -1.
        """
        if key in self.cache:
            node = self.cache[key]
            self.unlink(node)
            self.move_to_front(node)
            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        """
        Update or insert a key-value pair.
        Evict the least recently used key if capacity is exceeded.
        """
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.unlink(node)
            self.move_to_front(node)

        else:
            node = self.Node(key, value)
            self.cache[key] = node
            self.move_to_front(node)

            if len(self.cache) > self.capacity:
                self.remove_lru()

    def unlink(self, node: Node) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev

    def move_to_front(self, node: Node) -> None:
        """
        Insert node immediately after the head.
        """
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

    def remove_lru(self) -> None:
        """
        Remove the node immediately before the tail.
        """
        lru_node = self.tail.prev

        self.unlink(lru_node)
        del self.cache[lru_node.key]
