import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    cmd = input().rstrip()
    left, right = [], []
    
    for c in cmd:
        if c == "<":
            if left:
                right.append(left.pop())
        elif c == ">":
            if right:
                left.append(right.pop())
        elif c == "-":
            if left:
                left.pop()
        else:
            left.append(c)
    print("".join(left) + "".join(reversed(right)))
                
        
    