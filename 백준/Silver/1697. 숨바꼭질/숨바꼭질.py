from collections import deque

MAX = 100_000

n, k = map(int, input().split())

visited = [False] * (MAX + 1)
q = deque()

q.append((n, 0))
visited[n] = True

while q:
    x, t = q.popleft()

    if x == k:
        print(t)
        break

    for nx in (x - 1, x + 1, 2 * x):
        if 0 <= nx <= MAX and not visited[nx]:
            visited[nx] = True
            q.append((nx, t + 1))