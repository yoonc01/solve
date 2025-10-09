arr = [0 for _ in range(101)]

arr[1] = arr[2] = arr[3] = 1
arr[4] = arr[5] = 2

for i in range(6, 101):
    arr[i] = arr[i - 1] + arr[i - 5]

T = int(input())

for _ in range(T):
    print(arr[int(input())])