import sys

input = sys.stdin.readline

n = int(input())

ans = 0
stack = []
for _ in range(n):
    num = int(input())
    if num == 0:
        ans = ans - stack.pop()
    else:
        ans = ans + num
        stack.append(num)
        
print(ans)
    