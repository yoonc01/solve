from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
G = [list(map(int, input().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

def bfs(sx, sy):
    q = deque([(sx, sy)])
    visited[sx][sy] = True
    cnt = 1

    while q:
        x, y = q.popleft()
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and G[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    return cnt

sizes = []
for i in range(n):
    for j in range(n):
        if G[i][j] == 1 and not visited[i][j]:
            sizes.append(bfs(i, j))

sizes.sort()
print(len(sizes))
print(*sizes, sep="\n")