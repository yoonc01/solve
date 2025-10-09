n, m = map(int, input().split())

arr = []

def backtrack(s):
    if len(arr) == m:
        print(*arr)
        return
    for i in range(s, n + 1):
        arr.append(i)
        backtrack(i + 1)
        arr.pop()
        
backtrack(1)