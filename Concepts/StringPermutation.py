"""
Problem Statement
Given an input string, return all permutations of the string in an array.

Example 1:

string = 'ab'
output = ['ab', 'ba']
Example 2:

string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
"""


def permutations(s):
    return _permutation_func(s, 0)


def _permutation_func(s, index):
    if index >= len(s):
        return [""]
    else:
        output = []
        permutes = _permutation_func(s, index + 1)
        curr_char = s[index]

        for p in permutes:
            for j in range(len(p) + 1):
                new_p = p[0:j] + curr_char + p[j:]
                output.append(new_p)

        return output


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = permutations(string)

    print("Output ==> {}".format(output))

    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")


string = 'ab'
solution = ['ab', 'ba']
test_case = [string, solution]
test_function(test_case)


string = 'abc'
output = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
test_case = [string, output]
test_function(test_case)

string = 'abcd'
output = ['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']
test_case = [string, output]
test_function(test_case)