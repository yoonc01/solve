n = int(input())
arr = list(map(int, input().split()))
ans = []
arr = reversed(arr)

stack = []

for num in arr:
    while(stack and num >= stack[-1]):
        stack.pop()
    ans.append(stack[-1] if stack else -1)
    stack.append(num)
print(*reversed(ans))