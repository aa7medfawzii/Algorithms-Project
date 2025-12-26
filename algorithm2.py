"""
Name: Ahmed Mahmoud Fawzi Shaaban
ID: 100287413               Section: 2
algorithm2.py - Optimized Dynamic Programming Implementation
"""
def coin_change_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return -1 if dp[amount] == float('inf') else dp[amount]

import time

coins = list(map(int, input("Enter coins separated by space: ").split()))
amount = int(input("Enter amount: "))

start = time.time()
result = coin_change_dp(coins, amount)
end = time.time()

print("Result:", result)
print("Execution time:", (end - start), "seconds")