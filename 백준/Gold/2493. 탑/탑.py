import sys
input = sys.stdin.readline

n = int(input())
buildings = list(map(int, input().split()))
ans = [0 for _ in range(n)]
stack = []

for i, h in enumerate(buildings, start=1):
    while stack and stack[-1][1] < h:
        stack.pop()
    ans[i - 1] = stack[-1][0] if stack else 0
    stack.append((i, h))

print(*ans)