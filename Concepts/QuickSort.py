def sort_little_bit(items, start_index, end_index):
    left_index = start_index
    pivot_index = end_index
    pivot_value = items[pivot_index]

    while left_index != pivot_index:
        item = items[left_index]

        if item <= pivot_value:
            left_index += 1
            continue

        items[left_index] = items[pivot_index - 1]
        items[pivot_index - 1] = pivot_value
        items[pivot_index] = item
        pivot_index -= 1

    return pivot_index


def sort_all(items, start_index, end_index):
    if end_index <= start_index:
        return

    pivot_index = sort_little_bit(items, start_index, end_index)
    sort_all(items, start_index, pivot_index - 1)
    sort_all(items, pivot_index + 1, end_index)


def quick_sort(items):
    sort_all(items, 0, len(items) - 1)


items = [8, 3, 1, 7, 0, 10, 2]
print("Before sorting --> {}".format(items))
quick_sort(items)
print("After sorting --> {}".format(items))
