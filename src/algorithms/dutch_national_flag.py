def dutch_flag_partition(list_of_numbers: list[int], pivot_position: int) -> None:
    """
    The list_of_numbers will be sorted around the pivot position so that:
      - elements smaller will be moved to the left
      - elements bigger will be moved to the right
    :param list_of_numbers:
    :param pivot_position:
    :return: Nothing
    """
    pivot = list_of_numbers[pivot_position]

    # moving smaller elements to the left
    smaller = 0
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] < pivot:
            list_of_numbers[i], list_of_numbers[smaller] = list_of_numbers[smaller], list_of_numbers[i]
            smaller += 1

    larger = len(list_of_numbers) - 1
    for i in reversed(range(len(list_of_numbers))):
        if list_of_numbers[i] > pivot:
            list_of_numbers[i], list_of_numbers[larger] = list_of_numbers[larger], list_of_numbers[i]
            larger -= 1

# def dutch_flag_partition(list_of_numbers: list[int], pivot_position: int) -> None:
#     """
#     ChatGPT solution -- 20231126
#     Sorts the given list around a pivot such that:
#       - Elements smaller than the pivot are moved to the left
#       - Elements equal to the pivot are in the middle
#       - Elements bigger than the pivot are moved to the right
#
#     :param list_of_numbers: List of integers to be sorted
#     :param pivot_position: Index of the pivot element
#     :return: None
#     """
#     if pivot_position < 0 or pivot_position >= len(list_of_numbers):
#         raise ValueError("pivot_position out of bounds")
#
#     pivot = list_of_numbers[pivot_position]
#     low, mid, high = 0, 0, len(list_of_numbers) - 1
#
#     while mid <= high:
#         if list_of_numbers[mid] < pivot:
#             list_of_numbers[low], list_of_numbers[mid] = list_of_numbers[mid], list_of_numbers[low]
#             low, mid = low + 1, mid + 1
#         elif list_of_numbers[mid] > pivot:
#             list_of_numbers[mid], list_of_numbers[high] = list_of_numbers[high], list_of_numbers[mid]
#             high -= 1
#         else:
#             mid += 1


if __name__ == "__main__":
    l = [0, 2, 3, 1, 0, 2, 3, 2, 1]
    pos = 3
    dutch_flag_partition(l, pos)
    print(l)
