import sys

input = sys.stdin.readline

n = int(input())

dp = [sys.maxsize for _ in range(n + 1)]
prev = [0 for _ in range(n + 1)]
dp[1] = 0

for current_number in range(2, n + 1):
    dp[current_number] = dp[current_number - 1] + 1
    prev[current_number] = current_number - 1
    if (current_number % 2 == 0 and dp[current_number // 2] + 1 < dp[current_number]):
        dp[current_number] = dp[current_number // 2] + 1
        prev[current_number] = current_number // 2
    if (current_number % 3 == 0 and dp[current_number // 3] + 1 < dp[current_number]):
        dp[current_number] = dp[current_number // 3] + 1
        prev[current_number] = current_number // 3


path = []
node = n
while(node != 0):
    path.append(node)
    node = prev[node]

print(dp[n])
print(" ".join(map(str, path)))