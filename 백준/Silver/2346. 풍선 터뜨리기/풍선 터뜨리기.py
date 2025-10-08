from collections import deque

n = int(input())
temp_q = list(map(int, input().split()))
q = deque((i + 1, value) for i, value in enumerate(temp_q))

ans = []
while(True):
    num, val = q.popleft()
    ans.append(num)
    if not q:
        break
    if val > 0:
        for _ in range(val - 1):
            q.append(q.popleft())
    else:
        for _ in range(-val):
            q.appendleft(q.pop())

print(" ".join(map(str, ans)))