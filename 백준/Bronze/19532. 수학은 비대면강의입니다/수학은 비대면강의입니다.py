a, b, c, d, e, f = map(int, input().split())

ans_x, ans_y = 0, 0
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a * x + b * y == c and d * x + e * y == f:
            ans_x, ans_y = x, y

print(ans_x, ans_y)
