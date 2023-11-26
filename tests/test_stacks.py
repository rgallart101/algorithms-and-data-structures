from data_structures import (
    LinkedListStack,
    NativeStack,
    Node,
    create_list
)

def test_linkedlist_stacks():
    stack = LinkedListStack()

    stack.push(0)
    assert [0] == create_list(stack._items)

    stack.push(1)
    assert [0, 1] == create_list(stack._items)

    stack.push(2)
    assert [0, 1, 2] == create_list(stack._items)

    value = stack.peek()
    assert 2 == value

    value = stack.pop()
    assert 2 == value
    assert [0, 1] == create_list(stack._items)
    assert 2 == stack.size()

    stack.pop()
    stack.pop()
    assert stack._items._tail == stack._items._head == None
    assert 0 == stack.size()

def test_native_stacks():
    stack = NativeStack()

    stack.push(0)
    assert [0] == stack._items

    stack.push(1)
    assert [0, 1] == stack._items

    stack.push(2)
    assert [0, 1, 2] == stack._items

    value = stack.peek()
    assert 2 == value

    value = stack.pop()
    assert 2 == value
    assert [0, 1] == stack._items
    assert 2 == stack.size()

    stack.pop()
    stack.pop()
    assert 0 == stack.size()
