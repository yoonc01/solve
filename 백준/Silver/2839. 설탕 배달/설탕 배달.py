n = int(input())

ans = 5000

for i in range(n // 5 + 1):
    if (n - 5 * i) % 3 == 0:
        ans = min(ans, i + (n - 5 * i) // 3)
print(ans if ans != 5000 else -1)