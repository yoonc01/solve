from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    area = 1

    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and G[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
                area += 1
    return area

picture_cnt = 0
picture_big = 0

for i in range(n):
    for j in range(m):
        if G[i][j] == 1 and not visited[i][j]:
            picture_cnt += 1
            picture_big = max(picture_big, bfs(i, j))

print(picture_cnt)
print(picture_big)