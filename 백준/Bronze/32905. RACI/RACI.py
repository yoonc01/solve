import sys

input = sys.stdin.readline

n, m = map(int, input().split())

is_valid = True

for _ in range(n):
    task = input().split()
    accountable_count = task.count("A")

    if accountable_count != 1:
        is_valid = False
        break

print("Yes" if is_valid else "No")
