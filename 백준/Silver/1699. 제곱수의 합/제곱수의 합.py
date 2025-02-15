import sys

input = sys.stdin.readline

n = int(input())

dp = [i for i in range(n + 1)]  # 초기값을 i로 설정 (1로 다 더하는 경우)

# 제곱수 리스트 생성
squares = []
i = 1
while i * i <= n:
    squares.append(i * i)
    i += 1

# DP 테이블 갱신
for i in range(1, n + 1):
    for square in squares:
        if square > i:
            break
        dp[i] = min(dp[i], dp[i - square] + 1)

print(dp[n])
