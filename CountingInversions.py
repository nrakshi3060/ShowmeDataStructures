def count_inversions(arr):
    start_index = 0
    end_index = len(arr) - 1
    return count_inversions_func(arr, start_index, end_index)


def count_inversions_func(arr, start_index, end_index):
    if start_index >= end_index:
        return 0

    mid_index = start_index + (end_index - start_index) // 2

    left_count = count_inversions_func(arr, start_index, mid_index)

    right_count = count_inversions_func(arr, mid_index + 1, end_index)

    output = left_count + right_count

    output += merge(arr, start_index, mid_index, mid_index + 1, end_index)
    return output


def merge(arr, left_start_index, left_end_index, right_start_index, right_end_index):
    left_index = left_start_index
    right_index = right_start_index
    count = 0
    output = []

    while left_index <= left_end_index and right_index <= right_end_index:

        if arr[left_index] <= arr[right_index]:
            output.append(arr[left_index])
            left_index += 1
        else:
            count += left_end_index - left_index + 1
            output.append(arr[right_index])
            right_index += 1

    for i in range(left_index, left_end_index + 1):
        output.append(arr[i])

    for i in range(right_index, right_end_index + 1):
        output.append(arr[i])

    index = left_start_index
    for i in range(len(output)):
        arr[index] = output[i]
        index += 1

    return count


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]
    r = count_inversions(arr)
    print(r)
    if r == solution:
        print("Pass")
    else:
        print("Fail")


arr = [2, 5, 1, 3, 4]
solution = 4
test_case = [arr, solution]
test_function(test_case)

arr = [54, 99, 49, 22, 37, 18, 22, 90, 86, 33]
solution = 26
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, 4, 2, 3, 11, 22, 99, 108, 389]
solution = 2
test_case = [arr, solution]
test_function(test_case)
