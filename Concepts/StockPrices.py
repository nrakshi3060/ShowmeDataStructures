def max_returns(prices):
    """
    Calculate maxiumum possible return

    Args:
       prices(array): array of prices
    Returns:
       int: The maximum profit possible
    """
    max_transactions = 1
    t = [[0 for _ in range(len(prices))] for _ in range(max_transactions+1)]

    for i in range(1, max_transactions+1):
        max_diff = -prices[0]
        for j in range(1, len(prices)):
            t[i][j] = max(t[i][j - 1], max_diff + prices[j])
            max_diff = max(t[i - 1][j]-prices[j], max_diff)

    return t[-1][-1]


# Test Cases
def test_function(test_case):
    prices = test_case[0]
    solution = test_case[1]
    output = max_returns(prices)
    if output == solution:
        print("Pass")
    else:
        print("Fail")


prices = [2, 2, 7, 9, 9, 12, 18, 23, 34, 37, 45, 54, 78]
solution = 76
test_case = [prices, solution]
test_function(test_case)

prices = [3, 4, 7, 8, 6]
solution = 5
test_case = [prices, solution]
test_function(test_case)