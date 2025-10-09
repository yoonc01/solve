import sys

input = sys.stdin.readline

def recursion(s, l, r):
    global cnt
    cnt = cnt + 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)
    
T = int(input())

for _ in range(T):
    s = input().strip()
    cnt = 0
    print(recursion(s, 0, len(s) - 1), cnt)
