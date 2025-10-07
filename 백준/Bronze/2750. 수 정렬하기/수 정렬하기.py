T = int(input())

arr = []
for _ in range(T):
    n = int(input())
    arr.append(n)
    
arr.sort()
for i in range(T):
    print(arr[i])