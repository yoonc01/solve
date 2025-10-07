n = int(input())
arr = list(map(int, input().split()))

unduplicated_arr = sorted(set(arr))

d = {}
for idx, num in enumerate(unduplicated_arr):
    d[num] = idx

result = [d[num] for num in arr]

print(" ".join(map(str, result)))
