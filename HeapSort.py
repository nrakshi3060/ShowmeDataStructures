def heapify(arr, n, i):
    largest_index = i
    left_index = (2 * i) + 1
    right_index = (2 * i) + 2

    if left_index < n and arr[largest_index] < arr[left_index]:
        largest_index = left_index

    if right_index < n and arr[largest_index] < arr[right_index]:
        largest_index = right_index

    if largest_index != i:
        arr[i], arr[largest_index] = arr[largest_index], arr[i]
        heapify(arr, n, largest_index)


def heapsort(arr):
    # Given an array we start from the last element and do the heapify by inserting elements
    # So finally we will be getting max heap
    # Once we get the max heap we largest element and swap that with last element
    # Again we heapify recursively to fill the largest elements from the last index

    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr
    pass


arr = [3, 7, 4, 6, 1, 0, 9, 8, 9, 4, 3, 5]
print(heapsort(arr))
