class Node:
    def __init__(self, value=None) -> None:
        self._previous: Node = None
        self._next: Node = None
        self._value = value
