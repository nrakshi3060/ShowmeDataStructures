def isList(l):
    return isinstance(l, list)


def deep_reverse(l):
    return deep_reverse_func(l, 0)


def deep_reverse_func(l, index):
    if index >= len(l):
        return []
    output = deep_reverse_func(l, index + 1)
    if isList(l[index]):
        to_append = deep_reverse(l[index])
    else:
        to_append = l[index]
    output.append(to_append)
    return output


def test_function(test_case):
    arr = test_case[0]
    solution = test_case[1]

    output = deep_reverse(arr)
    if output == solution:
        print("Pass")
    else:
        print("False")


arr = [1, 2, 3, 4, 5]
solution = [5, 4, 3, 2, 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, 2, [3, 4, 5], 4, 5]
solution = [5, 4, [5, 4, 3], 2, 1]
test_case = [arr, solution]
test_function(test_case)

arr = [1, [2, 3, [4, [5, 6]]]]
solution = [[[[6, 5], 4], 3, 2], 1]
test_case = [arr, solution]
test_function(test_case)
