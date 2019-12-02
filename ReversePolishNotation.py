def evalRPN(tokens):
    """
    :type tokens: List[str]
    :rtype: int
    """
    stack = []
    first = 0
    second = 0
    output = 0

    for e in tokens:
        if e == '*':
            first = stack.pop()
            second = stack.pop()
            output = second * first
            stack.append(output)
        elif e == '/':
            first = stack.pop()
            second = stack.pop()
            output = int(second / first)
            stack.append(output)
        elif e == '+':
            first = stack.pop()
            second = stack.pop()
            output = second + first
            stack.append(output)
        elif e == '-':
            first = stack.pop()
            second = stack.pop()
            output = second - first
            stack.append(output)
        else:
            stack.append(int(e))

    output = stack.pop()
    print(output)
    return output


def test_function(test_case):
    output = evalRPN(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")


test_case_1 = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]

test_function(test_case_1)
