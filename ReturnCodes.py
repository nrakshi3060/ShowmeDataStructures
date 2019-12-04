def get_character(num):
    return chr(num + 96)

def return_codes(num):

    if num <= 0:
        return [""]

    remainder = num % 100

    output_100 = []
    output_10 = []

    if remainder <= 26 and num > 9:
        output_100 = return_codes(num // 100)
        r = get_character(remainder)
        for i, element in enumerate(output_100):
            new_element = element + r
            output_100[i] = new_element

    output_10 = return_codes(num//10)
    last_digit = num % 10
    r = get_character(last_digit)

    for i, element in enumerate(output_10):
        output_10[i] = element + r

    output = []
    output.extend(output_10)
    output.extend(output_100)
    return output


def test_function(test_case):
    number = test_case[0]
    solution = test_case[1]

    output = return_codes(number)
    print("output ==>{}".format(output))
    output.sort()
    solution.sort()

    if output == solution:
        print("Pass")
    else:
        print("Fail")

number = 123
solution = ['abc', 'aw', 'lc']
test_case = [number, solution]
test_function(test_case)