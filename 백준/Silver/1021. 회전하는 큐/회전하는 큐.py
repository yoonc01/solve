from collections import deque

n, m = map(int, input().split())
targets = list(map(int, input().split()))

dq = deque([i + 1 for i in range(n)])

ans = 0
for target in targets:
    rotate_cnt = 0
    while(dq[0] != target):
        rotate_cnt += 1
        dq.rotate(1)
    ans = ans + min(rotate_cnt, len(dq) - rotate_cnt)
    dq.popleft()
    
print(ans)