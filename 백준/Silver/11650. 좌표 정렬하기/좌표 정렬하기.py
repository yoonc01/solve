n = int(input())

arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort()

for x, y in arr:
    print(x, y)