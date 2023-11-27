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

    my_list = [0, 2, 3, 1, 0, 2, 3, 2, 1]
    pivot_position = 0

    dutch_flag_partition(my_list, pivot_position)

    assert my_list == [0, 0, 2, 3, 1, 2, 3, 2, 1]

    my_list = [0, 2, 3, 1, 0, 2, 3, 2, 1]
    pivot_position = 1

    dutch_flag_partition(my_list, pivot_position)

    assert my_list == [0, 1, 0, 1, 2, 2, 2, 3, 3]

    my_list = [0, 2, 3, 1, 0, 2, 3, 2, 1]
    pivot_position = 2

    dutch_flag_partition(my_list, pivot_position)

    assert my_list == [0, 2, 1, 0, 2, 2, 1, 3, 3]

    my_list = [0, 2, 3, 1, 0, 2, 3, 2, 1]
    pivot_position = 3

    dutch_flag_partition(my_list, pivot_position)

    assert my_list == [0, 0, 1, 1, 3, 2, 2, 3, 2]
