def create_list(ll) -> list:
    l = []
    n = ll._head
    while True:
        l.append(n._value)
        n = n._next
        if not n:
            break
    return l
