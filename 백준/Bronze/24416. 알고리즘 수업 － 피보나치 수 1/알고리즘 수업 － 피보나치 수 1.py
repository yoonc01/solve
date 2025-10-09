n = int(input())

arr = [0 for i in range(n + 1)]
arr[1] = 1
arr[2] = 1
for i in range(3, n + 1):
    arr[i] = arr[i - 1] + arr[i - 2]

print(arr[n], n - 2)