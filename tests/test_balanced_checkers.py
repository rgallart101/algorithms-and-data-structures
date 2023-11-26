from algorithms import (
    balanced_checker_native,
    balanced_checker_linkdelist
)

def test_balanced_checker_native():
    symbol_string = "{([])}"

    result = balanced_checker_native(symbol_string)

    assert True == result

def test_balanced_checker_linked_list():
    symbol_string = "{([])}"

    result = balanced_checker_linkdelist(symbol_string)

    assert True == result
