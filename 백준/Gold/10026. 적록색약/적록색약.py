from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

def canGo(x, y):
    return 0 <= x < n and 0 <= y < n

G = [list(input().strip()) for _ in range(n)]

visited_RG = [[False for _ in range(n)] for _ in range(n)]
visited_not_RG = [[False for _ in range(n)] for _ in range(n)]

cnt_RG = 0
cnt_not_RG = 0
for i in range(n):
    for j in range(n):
        if not visited_RG[i][j]:
            cnt_RG += 1
            q = deque()
            q.append((i, j))
            visited_RG[i][j] = True
            while(q):
                x, y = q.popleft()
                color = G[x][y]
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    
                    if canGo(nx, ny) and G[nx][ny] == color and not visited_RG[nx][ny]:
                        q.append((nx, ny))
                        visited_RG[nx][ny] = True
        if not visited_not_RG[i][j]:
            cnt_not_RG += 1
            q = deque()
            q.append((i, j))
            visited_not_RG[i][j] = True
            while(q):
                x, y = q.popleft()
                color = G[x][y]
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    
                    if canGo(nx, ny) and not visited_not_RG[nx][ny]:
                        if (color == "R" or color == "G") and (G[nx][ny] == "R" or G[nx][ny] == "G"):
                            q.append((nx, ny))
                            visited_not_RG[nx][ny] = True
                        if color == "B" and G[nx][ny] == "B":
                            q.append((nx, ny))
                            visited_not_RG[nx][ny] = True
print(cnt_RG, cnt_not_RG)                        