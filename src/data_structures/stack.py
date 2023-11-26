from .node import Node
from .linkedlist import LinkedList

class LinkedListStack:
    def __init__(self) -> None:
        self._items = LinkedList()

    def push(self, item):
        node = Node(item)
        self._items.add_with_node(self._items._tail, node)

    def pop(self):
        node = self._items.remove_tail()
        return node._value

    def peek(self):
        node = self._items.peek()
        return node._value

    def size(self):
        return self._items.size()

    def is_empty(self):
        return self.size() == 0


class NativeStack:
    def __init__(self) -> None:
        self._items = []

    def is_empty(self):
        return self._items == []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[self.size() - 1]

    def size(self):
        return len(self._items)
