import sys

input = sys.stdin.readline

w = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

def recursive(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        a, b, c = 20, 20, 20
    if w[a][b][c] == 0:    
        if a == 0 or b == 0 or c == 0:
            w[a][b][c] = 1
        elif a < b and b < c:
            w[a][b][c] = recursive(a, b, c - 1) + recursive(a, b - 1, c - 1) - recursive(a, b - 1, c)
        else:
            w[a][b][c] = recursive(a - 1, b, c) + recursive(a - 1, b - 1, c) + recursive(a - 1, b, c - 1) - recursive(a - 1, b - 1, c - 1)
    return w[a][b][c]


while(True):
    a, b, c = map(int, input().split())
    
    if a == b == c == -1:
        break
    print(f"w({a}, {b}, {c}) = {recursive(a, b, c)}")
    