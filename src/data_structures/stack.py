from .utils import create_list
from .node import Node
from .linkedlist import LinkedList

class Stack:
    def __init__(self) -> None:
        self._data = LinkedList()

    def push(self, node: Node):
        self._data.add_with_node(self._data._tail, node)

    def pull(self):
        return self._data.remove_tail()

    def peek(self):
        return self._data.peek()
