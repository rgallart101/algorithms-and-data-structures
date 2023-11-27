from algorithms import (
    dutch_flag_partition,
)


def test_dutch_flag_partition():
    my_list = [0, 1, 1, 0, 2, 1, 2, 0, 2]
    pivot_position = 1

    dutch_flag_partition(my_list, pivot_position)

    assert my_list == [0, 0, 0, 1, 1, 1, 2, 2, 2]

    my_list = [1, 0, 1, 1, 1, 2, 1, 0, 0, 0, 2]
    pivot_position = 4

    dutch_flag_partition(my_list, pivot_position)

    assert my_list == [0, 0, 0, 0, 1, 1, 1, 1, 1, 2, 2]
