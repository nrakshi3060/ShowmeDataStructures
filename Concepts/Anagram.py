def anagram_checker(str1, str2):
    """
    The goal of this exercise is to write some code to determine if two strings are anagrams of each other.

    An anagram is a word (or phrase) that is formed by rearranging the letters of another word (or phrase).

    For example:

    "rat" is an anagram of "art"
    "alert" is an anagram of "alter"
    "Slot machines" is an anagram of "Cash lost in me"
    Your function should take two strings as input and return True if the two words are anagrams and False if they are not.

    You can assume the following about the input strings:

    No punctuation
    No numbers
    No special characters

    """
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    return sorted(str1) == sorted(str2)


print("Pass" if not (anagram_checker('water', 'waiter')) else "Fail")
print("Pass" if anagram_checker('Dormitory', 'Dirty room') else "Fail")
print("Pass" if anagram_checker('Slot machines', 'Cash lost in me') else "Fail")
print("Pass" if not (anagram_checker('A gentleman', 'Elegant men')) else "Fail")
print("Pass" if anagram_checker('Time and tide wait for no man', 'Notified madman into water') else "Fail")
