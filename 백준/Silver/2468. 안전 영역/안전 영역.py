from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
G = [list(map(int, input().split())) for _ in range(n)]

def can_go(x, y):
    return 0 <= x < n and 0 <= y < n

ans = 1
for h in range(1, 101):
    at_least_one_plus = False
    for i in range(n):
        for j in range(n):
            G[i][j] -= 1
            if G[i][j] > 0:
                at_least_one_plus = True
                
    if at_least_one_plus == False:
        break
            
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if G[i][j] > 0 and not visited[i][j]:
                q = deque()
                q.append((i, j))
                visited[i][j] = True
                cnt += 1
                while(q):
                    x, y  = q.popleft()
                    
                    for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
                        nx, ny = x + dx, y + dy
                        
                        if can_go(nx, ny) and G[nx][ny] > 0 and not visited[nx][ny]:
                            q.append((nx, ny))
                            visited[nx][ny] = True
    ans = max(ans, cnt)
print(ans)
    