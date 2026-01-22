from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
G = [list(input().strip()) for _ in range(n)]
dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))

def bfs_count(is_color_blind: bool) -> int:
    visited = [[False] * n for _ in range(n)]
    cnt = 0

    def same(a: str, b: str) -> bool:
        if not is_color_blind:
            return a == b
        # 적록색약: R/G는 같은 색 취급
        if a == 'B' or b == 'B':
            return a == b
        return True  # a,b ∈ {R,G}

    for sx in range(n):
        for sy in range(n):
            if visited[sx][sy]:
                continue

            cnt += 1
            start_color = G[sx][sy]
            q = deque([(sx, sy)])
            visited[sx][sy] = True

            while q:
                x, y = q.popleft()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        if same(start_color, G[nx][ny]):
                            visited[nx][ny] = True
                            q.append((nx, ny))
    return cnt

normal = bfs_count(False)
color_blind = bfs_count(True)

print(normal, color_blind)