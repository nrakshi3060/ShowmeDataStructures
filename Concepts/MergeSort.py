def mergesort(arr):
    start_index = 0
    end_index = len(arr) - 1

    return mergesort_func(arr, start_index, end_index)


def mergesort_func(arr, start_index, end_index):
    if start_index == end_index:
        return [arr[start_index]]
    elif start_index > end_index:
        return []

    mid_index = start_index + (end_index - start_index) // 2
    left = mergesort_func(arr, start_index, mid_index)
    right = mergesort_func(arr, mid_index + 1, end_index)

    return merge(left, right)


def merge(left, right):
    merged = []
    right_index = 0
    left_index = 0

    # print("left {}".format(left))
    # print("right {}".format(right))

    while left_index < len(left) and right_index < len(right):

        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    for i in range(left_index, len(left)):
        merged.append(left[i])

    for i in range(right_index, len(right)):
        merged.append(right[i])

    return merged


test_list_1 = [8, 3, 1, 7, 0, 10, 2]
test_list_2 = [1, 0]
test_list_3 = [97, 98, 99]
test_list_4 = []
test_list_5 = [6]
print('{} to {}'.format(test_list_1, mergesort(test_list_1)))
print('{} to {}'.format(test_list_2, mergesort(test_list_2)))
print('{} to {}'.format(test_list_3, mergesort(test_list_3)))
print('{} to {}'.format(test_list_4, mergesort(test_list_4)))
print('{} to {}'.format(test_list_5, mergesort(test_list_5)))
