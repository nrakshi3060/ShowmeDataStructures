def staircase(n):
    if n <= 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return staircase(n - 3) + staircase(n - 2) + staircase(n - 1)


def test_function(test_case):
    n = test_case[0]
    solution = test_case[1]
    output = staircase(n)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


n = 3
solution = 4
test_case = [n, solution]
test_function(test_case)


n = 4
solution = 7
test_case = [n, solution]
test_function(test_case)

n = 7
solution = 44
test_case = [n, solution]
test_function(test_case)
