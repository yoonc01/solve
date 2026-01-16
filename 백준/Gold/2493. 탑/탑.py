n = int(input())
buildings = list(map(int, input().split()))
ans = [0 for _ in range(n)]
stack = []

for idx in range(n):
    while(stack and buildings[idx] > stack[-1][1]):
        stack.pop()
    ans[idx] = stack[-1][0] if stack else 0
    stack.append((idx + 1, buildings[idx]))

print(*ans)