n = int(input())

number_set = set(map(int, input().split()))

m = int(input())

check = list(map(int, input().split()))

ans = [0 for _ in range(m)]

for idx, number in enumerate(check):
    if number in number_set:
        ans[idx] = 1
        
print(" ".join(map(str, ans)))