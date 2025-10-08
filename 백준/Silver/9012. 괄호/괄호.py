import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    string = input().strip()

    is_ok = True
    stack = []
    for ch in string:
        if ch == "(":
            stack.append("(")
        else:
            if (len(stack) == 0):
                is_ok = False
                break
            else:
                stack.pop()
            
    if is_ok and len(stack) == 0:
        print("YES")
    else:
        print("NO")