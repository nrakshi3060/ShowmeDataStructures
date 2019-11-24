# Problem Statement
# Given an input array and a target value (integer), find two values in the array whose sum is equal to the target value. Solve the problem without using extra space. You can assume the array has unique values and will never have more than one solution.

def pair_sum(arr, target):
    """
    :param: arr - input array
    :param: target - target value
    TODO: complete this method to find two numbers such that their sum is equal to the target
    Return the two numbers in the form of a sorted list
    """

    arr.sort()

    start_index = 0
    end_index = len(arr) - 1

    while start_index < end_index:
        start = arr[start_index]
        end = arr[end_index]

        if start + end == target:
            return [start, end]
        elif start + end < target:
            start_index += 1
        else:
            end_index -= 1
    return [None, None]

    pass


def test_function(test_case):
    input_list = test_case[0]
    target = test_case[1]
    solution = test_case[2]
    output = pair_sum(input_list, target)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("False")


input_list = [2, 7, 11, 15]
target = 9
solution = [2, 7]
test_case = [input_list, target, solution]
test_function(test_case)

input_list = [0, 8, 5, 7, 9]
target = 9
solution = [0, 9]
test_case = [input_list, target, solution]
test_function(test_case)

input_list = [110, 9, 89]
target = 9
solution = [None, None]
test_case = [input_list, target, solution]
test_function(test_case)
