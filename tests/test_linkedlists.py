from data_structures import (
    LinkedList,
    Node,
    create_list
)

def test_linkedlists():
    node = Node()
    node._value = 1

    ll = LinkedList()
    ll.add(node=node)
    assert [1] == create_list(ll)
    assert node == ll._tail

    node = Node()
    node._value = 2
    ll.append(node=node)
    assert [1, 2] == create_list(ll)
    assert node == ll._tail

    node = Node()
    node._value = 4
    ll.append(node=node)
    assert [1, 2, 4] == create_list(ll)
    assert node == ll._tail

    node = Node()
    node._value = 3
    ll.insert(node=node, position=2)
    assert [1, 2, 3, 4] == create_list(ll)
    assert 4 == ll._tail._value

    LinkedList.reverse(ll)
    assert [4, 3, 2, 1] == create_list(ll)

    node_0 = Node(0)

    ll = LinkedList()
    ll.add_with_node(None, node_0)
    assert [0] == create_list(ll)
    assert node_0 == ll._tail == ll._head

    node_1 = Node(1)
    ll.add_with_node(node_0, node_1)
    assert [0, 1] == create_list(ll)
    assert node_0 == ll._head
    assert node_1 == ll._tail

    node_3 = Node(3)
    ll.add_with_node(node_1, node_3)
    assert [0, 1, 3] == create_list(ll)
    assert node_0 == ll._head
    assert node_3 == ll._tail

    node_2 = Node(2)
    ll.add_with_node(node_1, node_2)
    assert [0, 1, 2, 3] == create_list(ll)
    assert node_0 == ll._head
    assert node_3 == ll._tail

    LinkedList.reverse(ll)
    assert [3, 2, 1, 0] == create_list(ll)

    assert 4 == ll._len

    node = ll.remove_tail()
    assert 0 == node._value
    assert 3 == ll._len

    node = ll.remove_tail()
    node = ll.remove_tail()
    assert 2 == node._value
    assert 1 == ll._len

    node = ll.remove_tail()
    assert 3 == node._value
    assert 0 == ll._len
