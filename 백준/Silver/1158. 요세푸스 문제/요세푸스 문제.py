from collections import deque

n, k = map(int, input().split())

q = deque([i + 1 for i in range(n)])

ans = []
while(q):
    q.rotate(-k + 1)
    ans.append(q.popleft())
    
print(f"<{', '.join(map(str, ans))}>")