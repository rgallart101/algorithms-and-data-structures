from .utils import create_list
from .node import Node


class LinkedList:
    def __init__(self) -> None:
        self._head: Node = None
        self._tail: Node = None
        self._len = 0

    def add_with_node(self, prev_node: Node, node: Node):
        if not prev_node:
            self._head = self._tail = node
        elif not prev_node._next:
            prev_node._next = node
            node._previous = prev_node
            self._tail = node
        else:  # add between nodes
            next_node = prev_node._next
            prev_node._next = node
            node._previous = prev_node
            node._next = next_node
            next_node._previous = node

        self._len += 1

    def remove_tail(self) -> Node:
        # Creating a copy of the value. This is so we don't
        # return the previous or next element of the node.
        node: Node = Node()
        if self._tail:
            node._value = self._tail._value
            if not self._tail._previous:
                self._head = None
                self._tail = None
                self._len = 0
            else:
                previous_node = self._tail._previous
                previous_node._next = None
                self._tail = previous_node
                self._len -= 1
        else:
            node = None

        return node

    def remove_head(self) -> Node:
        # Creating a copy of the value. This is so we don't
        # return the previous or next element of the node.
        node: Node = Node()
        if self._head:
            node._value = self._head._value
            if not self._head._next:
                self._head = None
                self._tail = None
                self._len = 0
            else:
                next_node = self._head._next
                next_node._previous = None
                self._head = next_node
                self._len -= 1
        else:
            node = None

        return node

    def peek(self, tail: bool=True) -> Node:
        if tail:
            if self._tail:
                return Node(self._tail._value)
        else:
            if self._head:
                return Node(self._head._value)

        return None

    def add(self, node: Node) -> None:
        self.append(node=node)

    def append(self, node: Node) -> None:
        self.insert(node=node, position=self._len)

    def insert(self, node: Node, position: int=0) -> None:
        if not self._head:
            self._head = node
            self._tail = node
            self._len += 1
            return

        if position < 0:
            raise ValueError("Position must be >= 0")

        if position > self._len:
            raise ValueError(f"Position must be <= {self._len}")

        i = 0
        previous = None
        current = None
        if position == self._len:
            # Optimizing for append operations, as we already track the tail
            # element.
            previous = self._tail
        else:
            current = self._head
            while i < position:
                previous = current
                current = current._next
                i += 1

        # Insert the node
        node._next = previous._next
        node._previous = previous
        # Update the current node to point to node
        previous._next = node
        # Update the following node to point to node, if not None
        if current:
            current._previous = node
        else:
            self._tail = node
        # Add one to the LL length
        self._len += 1

    def size(self):
        return self._len

    @staticmethod
    def reverse(linked_list):
        first = linked_list._head
        last = linked_list._tail
        current = linked_list._head

        while True:
            current._next, current._previous = current._previous, current._next
            if not current._previous:
                break

            current = current._previous

        linked_list._tail = first
        linked_list._head = current
