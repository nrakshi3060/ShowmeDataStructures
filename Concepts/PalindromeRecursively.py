def is_palindrome_func(s):
    if len(s) <= 1:
        return True
    else:
        first_char = s[0]
        last_char = s[-1]

        sub_str = s[1:-1]

        return (first_char == last_char) and is_palindrome_func(sub_str)


def is_palindrome(s: str) -> bool:
    s1 = ""
    for char in s:
        if char.isalnum():
            s1 += char
    s1 = s1.lower()
    return is_palindrome_func(s1)


print("Pass" if (is_palindrome("")) else "Fail")
print("Pass" if (is_palindrome("a")) else "Fail")
print("Pass" if (is_palindrome("madam")) else "Fail")
print("Pass" if (is_palindrome("abba")) else "Fail")
print("Pass" if not (is_palindrome("Udacity")) else "Fail")
