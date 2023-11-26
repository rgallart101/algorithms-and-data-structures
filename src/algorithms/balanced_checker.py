from data_structures import (
    NativeStack,
    LinkedListStack,
)

def balanced_checker(s, symbol_string):
    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "[({":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index += 1

    if balanced and s.is_empty():
        return True

    return False


def matches(open, close):
    opens = "[({"
    closers = "])}"

    return opens.index(open) == closers.index(close)


def balanced_checker_native(symbol_string):
    s = NativeStack()
    return balanced_checker(s, symbol_string)


def balanced_checker_linkdelist(symbol_string):
    s = LinkedListStack()
    return balanced_checker(s, symbol_string)
