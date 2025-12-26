"""
Name: Ahmed Mahmoud Fawzi Shaaban
ID: 1000287413           Section: 2
algorithm1.py - Naive Recursive Implementation
"""
def coin_change_naive(coins, amount):
    if amount == 0:
        return 0
    if amount < 0:
        return float('inf')

    min_coins = float('inf')

    for coin in coins:
        result = coin_change_naive(coins, amount - coin)
        if result != float('inf'):
            min_coins = min(min_coins, result + 1)

    return min_coins

# wrapper to match problem requirements
def solve(coins, amount):
    result = coin_change_naive(coins, amount)
    return -1 if result == float('inf') else result

import time

coins = list(map(int, input("Enter coins separated by space: ").split()))
amount = int(input("Enter amount: "))

start = time.time()
result = solve(coins, amount)
end = time.time()

print("Result:", result)

print("Execution time:", (end - start), "seconds")
