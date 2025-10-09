import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]

zeros = [(i, j) for i in range(9) for j in range(9) if board[i][j] == 0]

def is_possible(r, c, num):
    for i in range(9):
        if board[r][i] == num or board[i][c] == num:
            return False

    sr, sc = (r // 3) * 3, (c // 3) * 3
    for i in range(sr, sr + 3):
        for j in range(sc, sc + 3):
            if board[i][j] == num:
                return False
    return True


def backtrack(idx):
    if idx == len(zeros):
        for row in board:
            print(*row)
        sys.exit(0)

    r, c = zeros[idx]
    for num in range(1, 10):
        if is_possible(r, c, num):
            board[r][c] = num
            backtrack(idx + 1)
            board[r][c] = 0

backtrack(0)
