import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]

mean = round(sum(arr) / n)

arr.sort()
median = arr[n // 2]

counter = Counter(arr).most_common()
max_freq = counter[0][1]
modes = [num for num, freq in counter if freq == max_freq]
modes.sort()
mode = modes[0] if len(modes) == 1 else modes[1]

range_val = arr[-1] - arr[0]

print(mean)
print(median)
print(mode)
print(range_val)
