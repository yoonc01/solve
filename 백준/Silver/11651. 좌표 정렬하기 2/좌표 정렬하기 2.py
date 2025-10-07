n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]


arr.sort(key=lambda p: (p[1], p[0]))

for x, y in arr:
    print(x, y)
