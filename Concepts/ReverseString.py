def string_reverser(input_string):
    """
    In this first exercise, the goal is to write a function that takes a string as input and then returns the reversed string.

    For example, if the input is the string "water", then the output should be "retaw".

    While you're working on the function and trying to figure out how to manipulate the string, it may help to use the print statement so you can see the effects of whatever you're trying.
    """
    output_string = ""
    for i in range(len(input_string)):
        output_string += input_string[(len(input_string) - 1) - i]

    print(output_string)
    return output_string


print("Pass" if ('retaw' == string_reverser('water')) else "Fail")
print("Pass" if ('!noitalupinam gnirts gnicitcarP' == string_reverser('Practicing string manipulation!')) else "Fail")
print("Pass" if ('3432 :si edoc esuoh ehT' == string_reverser('The house code is: 2343')) else "Fail")
