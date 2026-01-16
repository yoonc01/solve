import sys

input = sys.stdin.readline

n = int(input())
current = 1

stack = []
ans = []
is_possible = True

for _ in range(n):
    num = int(input())
    if current > num:
        if num == stack[-1]:
            stack.pop()
            ans.append("-")
        else:
            is_possible = False
            break
    else:
        while(current <= num):
            stack.append(current)
            ans.append("+")
            current += 1
        
        stack.pop()
        ans.append("-")
            
if is_possible:
    print("\n".join(ans))
else:
    print("NO")
        
        