import sys

input = sys.stdin.readline

n = int(input())

arr = [0 for _ in range(10_001)]

for _ in range(n):
    num = int(input())
    arr[num] = arr[num] + 1

for num, repeat in enumerate(arr):
    for _ in range(repeat):
        print(num)