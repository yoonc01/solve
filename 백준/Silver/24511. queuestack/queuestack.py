n = int(input())
queuestack = list(map(int, input().split()))
values = list(map(int, input().split()))

n = int(input())
c = list(map(int, input().split()))

ans = []

for t, value in zip(queuestack, values):
    if t == 0:
        ans.append(value)
ans = ans[::-1] + c

print(" ".join(map(str, ans[:n])))