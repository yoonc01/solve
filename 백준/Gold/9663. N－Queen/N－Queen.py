n = int(input())
ans = 0

cols = set()          # 사용 중인 열
diag1 = set()         # ↘ 방향 대각선 (row + col)
diag2 = set()         # ↙ 방향 대각선 (row - col)

def backtrack(row):
    global ans
    if row == n:
        ans += 1
        return
    for col in range(n):
        if col in cols or (row + col) in diag1 or (row - col) in diag2:
            continue
        cols.add(col)
        diag1.add(row + col)
        diag2.add(row - col)
        backtrack(row + 1)
        cols.remove(col)
        diag1.remove(row + col)
        diag2.remove(row - col)

backtrack(0)
print(ans)
