from data_structures import (
    Stack,
    Node,
    create_list
)

def test_stacks():
    stack = Stack()

    node = Node(0)
    stack.push(node=node)
    assert [0] == create_list(stack._data)

    node = Node(1)
    stack.push(node=node)
    assert [0, 1] == create_list(stack._data)

    node = Node(2)
    stack.push(node=node)
    assert [0, 1, 2] == create_list(stack._data)

    node = stack.peek()
    assert 2 == node._value

    node = stack.pull()
    assert 2 == node._value
    assert [0, 1] == create_list(stack._data)
    assert 2 == stack._data._len

    stack.pull()
    stack.pull()
    assert stack._data._tail == stack._data._head == None
    assert 0 == stack._data._len
