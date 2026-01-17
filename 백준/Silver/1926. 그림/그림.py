from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
G = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
picture_cnt = 0
picture_big = 0

def canGo(x, y):
    return 0 <= x < n and 0 <= y < m and G[x][y] and not visited[x][y]

def bfs(a, b):
    global picture_big
    q = deque()
    big = 1
    q.append((a, b))
    visited[a][b] = True
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]

    while(q):
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if canGo(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True
                big += 1
    picture_big = max(picture_big, big)
    
for i in range(n):
    for j in range(m):
        if G[i][j] == 1 and not visited[i][j]:
            bfs(i, j)
            picture_cnt += 1
            
print(picture_cnt)
print(picture_big)

    