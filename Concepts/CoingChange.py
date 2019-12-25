def coin_change(coins, amount):
    # Create a memo that will storing the fewest coins with given amount
    # that we have already calculated so that we do not have to do the
    # calculation again.
    memo = {}

    def return_change(remaining):
        # Base cases
        if remaining < 0:  return float('inf')
        if remaining == 0: return 0

        # Check if we have already calculated
        if remaining not in memo:
            # If not previously calculated, calculate it by calling return_change with the remaining amount
            memo[remaining] = min(return_change(remaining - c) + 1 for c in coins)
        return memo[remaining]

    res = return_change(amount)

    # return -1 when no change found
    return -1 if res == float('inf') else res


def test_function(test_case):
    arr = test_case[0]
    amount = test_case[1]
    solution = test_case[2]
    output = coin_change(arr, amount)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


arr = [1, 2, 5]
amount = 11
solution = 3
test_case = [arr, amount, solution]
test_function(test_case)
