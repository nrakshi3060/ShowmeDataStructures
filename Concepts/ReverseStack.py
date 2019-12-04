def reverse_stack(stack):
    holder_stack = []

    while len(stack) != 0:
        popped_element = stack.pop()
        holder_stack.append(popped_element)
    return __reverse_stack_func(stack, holder_stack)


def __reverse_stack_func(stack, holder_stack):
    if len(holder_stack) == 0:
        return
    popped_element = holder_stack.pop()
    __reverse_stack_func(stack, holder_stack)
    stack.append(popped_element)


def test_function(test_case):
    stack = []
    for num in test_case:
        stack.append(num)

    reverse_stack(stack)
    index = 0
    while not (len(stack) == 0):
        popped = stack.pop()
        if popped != test_case[index]:
            print("Fail")
            return
        else:
            index += 1
    print("Pass")


test_case_1 = [1, 2, 3, 4]
test_function(test_case_1)
