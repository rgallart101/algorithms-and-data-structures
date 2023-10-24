from .utils import create_list
from .node import Node
from .linkedlist import LinkedList


class Queue:
    def __init__(self) -> None:
        self._data = LinkedList()

    def enqueue(self, node):
        self._data.add_with_node(self._data._tail, node)

    def dequeue(self) -> Node:
        return self._data.remove_head()

    def peek(self) -> Node:
        return self._data.peek(tail=False)
