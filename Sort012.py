# Problem Statement
# Write a function that takes an input array (or Python list) consisting of only 0s, 1s, and 2s, and sorts that array in a single traversal.
# Note that if you can get the function to put the 0s and 2s in the correct positions, this will aotumatically cause the 1s to be in the correct positions as well.

def sort_012(arr):
    start_index = 0
    next_pos_0 = 0
    next_pos_2 = len(arr) - 1

    while start_index <= next_pos_2:

        if arr[start_index] == 0:
            arr[start_index] = arr[next_pos_0]
            arr[next_pos_0] = 0
            next_pos_0 += 1
            start_index += 1
        elif arr[start_index] == 2:
            arr[start_index] = arr[next_pos_2]
            arr[next_pos_2] = 2
            next_pos_2 -= 1
        else:
            start_index += 1



def test_function(test_case):
    sort_012(test_case)
    print(test_case)
    if test_case == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_case = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
test_function(test_case)

test_case = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
test_function(test_case)

test_case = [2, 2, 0, 0, 2, 1, 0, 2, 2, 1, 1, 1, 0, 1, 2, 0, 2, 0, 1]
test_function(test_case)