def reverse_string(input_str):
    if len(input_str) == 0:
        return ""
    else:
        first_char = input_str[0]
        sub_str = input_str[1:]

        reversed_sub_str = reverse_string(sub_str)

        return reversed_sub_str + first_char


print("Pass" if ("" == reverse_string("")) else "Fail")
print("Pass" if ("cba" == reverse_string("abc")) else "Fail")
print("Pass" if ("HTIHSKAR" == reverse_string("RAKSHITH")) else "Fail")
