"""
Problem Statement
Given an input string consisting of only { and }, figure out the minimum number of reversals required to make the brackets balanced.

For example:

For input_string = "}}}}, the number of reversals required is 2.
For input_string = "}{}}, the number of reversals required is 1.
If the brackets cannot be balanced, return -1 to indicate that it is not possible to balance them.

example 1 input_str = "}}}}" converted_str = "{{}}" num_conversions = 2

example 2 input_str = "}{}}" converted_str ="{{}}" num_conversions = 1

example 3 input_str = "}}}" this can not be converted because in order to be blanced, total number of paranthesis should be even

example 4 input_str = "}{{}}{{{" converted_str = "{{{}}}{}" num_conversions = 3

Remove all the balanced part of the string and remaining will be }}..{{..

for example

input_str = "}{{}}{{{"
Remove balance part = "}{{{"

"""


def remove_balanced(input_str):
    stack = []
    for char in input_str:
        if char == '}' and len(stack) != 0:
            if stack[len(stack) - 1] == '{':
                stack.pop()
            else:
                stack.append(char)
        else:
            stack.append(char)

    return stack


def minimum_bracket_reversals(input_string):
    if len(input_string) % 2 == 1:
        return -1

    stack = remove_balanced(input_string)

    red_length = len(stack)

    n = 0
    while len(stack) != 0 and stack[len(stack) - 1] == '{':
        stack.pop()
        n += 1

    output = red_length // 2 + n % 2
    print(output)
    return output


def test_function(test_case):
    input_string = test_case[0]
    expected_output = test_case[1]
    output = minimum_bracket_reversals(input_string)

    if output == expected_output:
        print("Pass")
    else:
        print("Fail")


test_case_1 = ["}}}}", 2]
test_function(test_case_1)

test_case_2 = ["}}{{", 2]
test_function(test_case_2)

test_case_3 = ["{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{{}}}}}", 13]
test_function(test_case_3)

test_case_4 = ["}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{", 2]
test_function(test_case_4)

test_case_5 = ["}}{}{}{}{}{}{}{}{}{}{}{}{}{}{}", 1]
test_function(test_case_5)