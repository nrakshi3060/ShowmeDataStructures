"""
Problem Statement
Given an integer array, find and return all the subsets of the array. The order of subsets in the output array is not important. However the order of elements in a particular subset should remain the same as in the input array.

Note: An empty set will be represented by an empty list

Example 1

arr = [9]

output = [[]
          [9]]
Example 2

arr = [9, 12, 15]

output =  [[],
           [15],
           [12],
           [12, 15],
           [9],
           [9, 15],
           [9, 12],
           [9, 12, 15]]

1. if index >= len(list) then return empty list of list. Now pointer is in last index append the empty index previous return to the output and also create new subsetts using the current index
"""


def return_subsets(l):
    return return_subsets_func(l, 0)


def return_subsets_func(l, index):
    if index >= len(l):
        return [[]]
    else:
        small_output = return_subsets_func(l, index + 1)
        output = []

        # Add results of small output to output
        for element in small_output:
            output.append(element)

    for element in small_output:
        current_output = list()
        current_output.append(l[index])
        current_output.extend(element)
        output.append(current_output)

    return output


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = return_subsets(arr)
    print(output)
    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [5, 7]
solution = [[], [7], [5], [5, 7]]
test_case = [arr, solution]
test_function(test_case)