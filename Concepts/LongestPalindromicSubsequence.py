"""
Longest Palindromic Subsequence
In this notebook, you'll be tasked with finding the length of the Longest Palindromic Subsequence (LPS) given a string of characters.

As an example:

With an input string, ABBDBCACB
The LPS is BCACB, which has length = 5
In this notebook, we'll focus on finding an optimal solution to the LPS task, using dynamic programming. There will be some similarities to the Longest Common Subsequence (LCS) task, which is outlined in detail in a previous notebook. It is recommended that you start with that notebook before trying out this task.

Hint
Storing pre-computed values

The LPS algorithm depends on looking at one string and comparing letters to one another. Similar to how you compared two strings in the LCS (Longest Common Subsequence) task, you can compare the characters in just one string with one another, using a matrix to store the results of matching characters.

For a string on length n characters, you can create an n x n matrix to store the solution to subproblems. In this case, the subproblem is the length of the longest palindromic subsequence, up to a certain point in the string (up to the end of a certain substring).

It may be helpful to try filling up a matrix on paper before you start your code solution. If you get stuck with this task, you may look at some example matrices below (see the section titled Example matrices), before consulting the complete solution code.

Example matrices
Example LPS Subproblem matrix 1:

input_string = 'BANANO'

LPS subproblem matrix:

     B  A  N  A  N  O
B  [[1, 1, 1, 3, 3, 3],
A   [0, 1, 1, 3, 3, 3],
N   [0, 0, 1, 1, 3, 3],
A   [0, 0, 0, 1, 1, 1],
N   [0, 0, 0, 0, 1, 1],
O   [0, 0, 0, 0, 0, 1]]

LPS length:  3
Example LPS Subproblem matrix 2:

input_string = 'TACOCAT'

LPS subproblem matrix:

     T  A  C  O  C  A  T
T  [[1, 1, 1, 1, 3, 5, 7],
A   [0, 1, 1, 1, 3, 5, 5],
C   [0, 0, 1, 1, 3, 3, 3],
O   [0, 0, 0, 1, 1, 1, 1],
C   [0, 0, 0, 0, 1, 1, 1],
A   [0, 0, 0, 0, 0, 1, 1],
T   [0, 0, 0, 0, 0, 0, 1]]

LPS length:  7
Note: The lower diagonal values will remain 0 in all cases.

The matrix rules
You can efficiently fill up this matrix one cell at a time. Each grid cell only depends on the values in the grid cells that are directly on bottom and to the left of it, or on the diagonal/bottom-left. The rules are as follows:

Start with an n x n matrix where n is the number of characters in a given string; the diagonal should all have the value 1 for the base case, the rest can be zeros.
As you traverse your string:
If there is a match, fill that grid cell with the value to the bottom-left of that cell plus two.
If there is not a match, take the maximum value from either directly to the left or the bottom cell, and carry that value over to the non-match cell.
After completely filling the matrix, the top-right cell will hold the final LPS length.
"""


def lps(input_string):
    n = len(input_string)
    # create a matrix
    lookup_table = [[0 for _ in range(n)] for _ in range(n)]

    # since we know that diagonal of matrix represents sing letter
    for i in range(n):
        lookup_table[i][i] = 1

    for s_size in range(2, n + 1):
        for start_index in range(n - s_size + 1):
            end_index = start_index + s_size - 1
            if s_size == 2 and input_string[start_index] == input_string[end_index]:
                lookup_table[start_index][end_index] = 2
            elif input_string[start_index] == input_string[end_index]:
                lookup_table[start_index][end_index] = 2 + lookup_table[start_index + 1][end_index - 1]
            else:
                lookup_table[start_index][end_index] = max(lookup_table[start_index][end_index - 1],
                                                           lookup_table[start_index + 1][end_index])
    return lookup_table[0][n - 1]


def test_function(test_case):
    string = test_case[0]
    solution = test_case[1]
    output = lps(string)
    print(output)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


string = "TACOCAT"
solution = 7
test_case = [string, solution]
test_function(test_case)

string = 'BANANA'
solution = 5
test_case = [string, solution]
test_function(test_case)

string = 'BANANO'
solution = 3
test_case = [string, solution]
test_function(test_case)
