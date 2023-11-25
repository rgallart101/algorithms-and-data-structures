from .utils import create_list
from .node import Node
from .linkedlist import LinkedList

class LinkedListStack:
    def __init__(self) -> None:
        self._data = LinkedList()

    def push(self, node: Node):
        self._data.add_with_node(self._data._tail, node)

    def pop(self):
        return self._data.remove_tail()

    def peek(self):
        return self._data.peek()

    def size(self):
        return self._data.size()


class NativeStack:
    def __init__(self) -> None:
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[self.size() - 1]

    def size(self):
        return len(self.items)
