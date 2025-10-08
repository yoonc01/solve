from collections import deque

n, k = map(int, input().split())

ans = []
q = deque([i + 1 for i in range(n)])

while(q):
    for _ in range(k - 1):
        q.append(q.popleft())
    ans.append(q.popleft())
    
print(f"<{', '.join(map(str, ans))}>")