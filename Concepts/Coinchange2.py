import math


# Solution Two

# We initiate F[Amount] to be float('inf') and F[0] = 0
# Let F[Amount] to be the minimum number of coins needed to get change for the Amount.
# F[Amount + coin] = min(F(Amount + coin), F(Amount) + 1) if F[Amount] is reachable.
# F[Amount + coin] = F(Amount + coin) if F[Amount] is not reachable.

def coin_change(coins, amount):
    t = [math.inf for _ in range(amount + 1)]
    r = [-1 for _ in range(amount + 1)]

    t[0] = 0

    for j in range(len(coins)):
        for i in range(amount + 1):
            if i >= coins[j]:
                t[i] = min(t[i], t[i - coins[j]] + 1)
                r[i] = j

    if t[amount] != math.inf:
        printcombination(r, coins)
        return t[amount]
    else:
        return -1


def printcombination(r, coins):
    if r[-1] == -1:
        return "No possible solution"

    start = len(r) - 1
    l = []
    while start != 0:
        j = r[start]
        l.append(coins[j])
        start = start - coins[j]

    print(l)


def test_function(test_case):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = coin_change(arr, amount)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [1, 2, 3]
amount = 6
solution = 2
test_case = [arr, amount, solution]
test_function(test_case)

arr = [1, 2, 5]
amount = 11
solution = 3
test_case = [arr, amount, solution]
test_function(test_case)

arr = [5, 7, 8]
amount = 2
solution = -1
test_case = [arr, amount, solution]
test_function(test_case)
