import sys

input = sys.stdin.readline

n = int(input())

dp = [[sys.maxsize, [1]] for _ in range(n + 1)]
dp[1] = [0, [1]]

for current_number in range(2, n + 1):
    if (current_number % 3 == 0):
        prev_number = current_number // 3
        prev_cnt, prev_process = dp[prev_number]
        current_cnt, current_process = dp[current_number]
        if (prev_cnt + 1 < current_cnt):
            current_process = prev_process[:]
            current_process.append(current_number)
            dp[current_number] = [prev_cnt + 1, current_process]
    if (current_number % 2 == 0):
        prev_number = current_number // 2
        prev_cnt, prev_process = dp[prev_number]
        current_cnt, current_process = dp[current_number]
        if (prev_cnt + 1 < current_cnt):
            current_process = prev_process[:]
            current_process.append(current_number)
            dp[current_number] = [prev_cnt + 1, current_process]
    prev_number = current_number - 1
    prev_cnt, prev_process = dp[prev_number]
    current_cnt, current_process = dp[current_number]
    if (prev_cnt + 1 < current_cnt):
        current_process = prev_process[:]
        current_process.append(current_number)
        dp[current_number] = [prev_cnt + 1, current_process]
    
print(dp[n][0])
print(" ".join(map(str, dp[n][1][::-1])))

        

