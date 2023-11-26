from data_structures import (
    Queue,
    Node,
    create_list
)

def test_queues():
    queue = Queue()

    node = Node(0)
    queue.enqueue(node)
    assert [0] == create_list(queue._data)

    node = Node(1)
    queue.enqueue(node)
    assert [0, 1] == create_list(queue._data)

    node = Node(2)
    queue.enqueue(node)
    assert [0, 1, 2] == create_list(queue._data)

    node = queue.peek()
    assert 0 == node._value

    node = queue.dequeue()
    assert 0 == node._value
    assert [1, 2] == create_list(queue._data)
    assert 2 == queue._data._len

    queue.dequeue()
    queue.dequeue()
    assert queue._data._head == queue._data._tail == None
    assert 0 == queue._data._len
