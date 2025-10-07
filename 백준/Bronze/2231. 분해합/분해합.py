n = int(input())

start = max(0, n - 9 * len(str(n)))
result = 0

for i in range(start, n):
    if i + sum(map(int, str(i))) == n:
        result = i
        break

print(result)
