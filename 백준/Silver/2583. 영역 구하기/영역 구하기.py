from collections import deque
import sys

n, m, k = map(int, input().split())
G = [[1 for _ in range(m)] for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

for _ in range(k):
    x0, y0, x1, y1 = map(int, input().split())
    for i in range(y0, y1):
        for j in range(x0, x1):
            G[i][j] = 0

ans = 0
size = []

def can_go(x, y):
    return 0 <= x < n and 0 <= y < m

def bfs(a, b):
    q = deque()
    q.append((a, b))
    visited[a][b] = True
    cnt = 1
    while(q):
        x, y = q.popleft()
        
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nx, ny = x + dx, y + dy
            
            if (can_go(nx, ny) and G[nx][ny] and not visited[nx][ny]):
                q.append((nx, ny))
                visited[nx][ny] = True
                cnt += 1
    return cnt
        
ans = 0
for i in range(n):
    for j in range(m):
        if G[i][j] == 1 and not visited[i][j]:
            ans = ans + 1
            size.append(bfs(i, j))

size.sort()
print(ans)
print(*size)