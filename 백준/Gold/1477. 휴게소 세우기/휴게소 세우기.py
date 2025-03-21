import sys
import math

input = sys.stdin.readline

n, m, l = map(int, input().split())

arr = list(map(int, input().split()))
arr.append(l)

arr.sort()

low = 1
high = l - 1

def is_possible(value):
    prev = 0
    cnt = 0
    for curr in arr:
        diff = curr - prev
        if (diff > value):
            cnt = cnt + math.ceil(diff / value) - 1
        prev = curr
    return cnt <= m
        
ans = 0
while(low <= high):
    mid = (low + high) // 2
    if is_possible(mid):
        high = mid - 1
        ans = mid
    else:
        low = mid + 1
print(ans)