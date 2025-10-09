n = int(input())

arr = [0 for _ in range(n)]

ans = 0
def is_possible(idx):
    for i in range(idx):
        if arr[idx] - arr[i] == idx - i:
            return False
        elif arr[idx] - arr[i] == i - idx:
            return False
        elif arr[idx] == arr[i]:
            return False
    return True
     
def backtrack(idx):
    global ans
    if idx == n:
        ans = ans + 1
        return
    for i in range(n):
        arr[idx] = i
        if is_possible(idx):
            backtrack(idx + 1)
backtrack(0)
print(ans)
            