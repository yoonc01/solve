import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

dp_r = [arr[0][0] for _ in range(n)]
dp_g = [arr[0][1] for _ in range(n)]
dp_b = [arr[0][2] for _ in range(n)]

for i in range(1, n):
    dp_r[i] = min(dp_g[i - 1], dp_b[i - 1]) + arr[i][0]
    dp_g[i] = min(dp_r[i - 1], dp_b[i - 1]) + arr[i][1]
    dp_b[i] = min(dp_g[i - 1], dp_r[i - 1]) + arr[i][2]
    
print(min(dp_r[n - 1], dp_g[n - 1], dp_b[n - 1]))
