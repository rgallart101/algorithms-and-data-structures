def dutch_flag_partition(list_of_numbers: list[int], pivot_position: int) -> None:
    """
    The list_of_numbers will be sorted around the pivot position so that:
      - elements smaller will be moved to the left
      - elements bigger will be moved to the right
      - elements equal to the pivot will be in the middle
    :param list_of_numbers:
    :param pivot_position:
    :return: Nothing
    """
    first_pivot = last_pivot = 0
    bigger_found = False
    pivot_found = False
    pivot = list_of_numbers[pivot_position]
    index = 0

    while index < len(list_of_numbers):
        if list_of_numbers[index] < pivot:
            if pivot_found:
                list_of_numbers[first_pivot], list_of_numbers[index] = list_of_numbers[index], list_of_numbers[
                    first_pivot]
                first_pivot += 1
                if bigger_found:
                    list_of_numbers[last_pivot+1], list_of_numbers[index] = list_of_numbers[index], list_of_numbers[
                        last_pivot+1]
                    last_pivot += 1
                else:
                    last_pivot = index
        elif list_of_numbers[index] > pivot:
            if not bigger_found:
                bigger_found = True
        else:
            if not pivot_found:
                first_pivot = last_pivot = index
                pivot_found = True
            else:
                if bigger_found:
                    list_of_numbers[index-1], list_of_numbers[index] = list_of_numbers[index], list_of_numbers[
                        index-1]
                    last_pivot += 1
                else:
                    last_pivot = index

        index += 1

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
