n, m = map(int, input().split())

board = [input() for _ in range(n)]

ans = 64

def get_change(case, row, col):
    global ans
    cnt = 0
    for i in range(row, row + 8):
        for j in range(col, col + 8):
            if board[i][j] != case[(i + j) % 2]:
                cnt = cnt + 1
    ans = min(ans, cnt)
                
case_1 = ["B", "W"]
case_2 = ["W", "B"]
    
for i in range(n - 7):
    for j in range(m - 7):
        get_change(case_1, i, j)
        get_change(case_2, i, j)
        
print(ans)