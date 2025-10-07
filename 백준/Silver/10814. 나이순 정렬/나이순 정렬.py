n = int(input())

arr = []
for i in range(n):
    age, name = input().split()
    age = int(age)
    arr.append((age, i, name))
    
for age, idx, name in sorted(arr):
    print(age, name)
    
    