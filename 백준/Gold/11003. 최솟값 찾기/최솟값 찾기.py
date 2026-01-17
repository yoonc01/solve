from collections import deque

n, m = map(int, input().split())
arr = map(int, input().split())

dq = deque()
ans = []
for i, num in enumerate(arr):
    while(dq and dq[-1][1] > num):
        dq.pop()
    dq.append((i, num))
    while(dq and dq[0][0] < i - m + 1):
        dq.popleft()
    ans.append(dq[0][1])
print(*ans)