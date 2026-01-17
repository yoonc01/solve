from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cmds = input().rstrip()
    n = int(input())
    s = input().rstrip()

    if s == "[]":
        dq = deque()
    else:
        dq = deque(s[1:-1].split(','))
    
    front = True
    error = False
    for cmd in cmds:
        if cmd == "R":
            front = not front
        else:
            if dq:
                if front:
                    dq.popleft()
                else:
                    dq.pop()   
            else:
                error = True
                break

    if not front:
        dq = reversed(dq)
    if error:
        print("error")
    else:
        print(f"[{','.join(map(str, dq))}]")