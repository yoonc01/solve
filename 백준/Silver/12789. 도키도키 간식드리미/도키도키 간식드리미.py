from collections import deque

n = int(input())
q = deque(map(int, input().split()))

stack = []
state = "Nice"
number = 1

while(q or stack):
    if number in q:
        while(q[0] != number):
            stack.append(q.popleft())
        q.popleft()
    else:
        if stack[-1] == number:
            stack.pop()
        else:
            state = "Sad"
            break
    number = number + 1
print(state)