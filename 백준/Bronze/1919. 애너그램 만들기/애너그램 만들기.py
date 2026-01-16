def cnt_alpha(string):
    result = [0 for _ in range(26)]
    base = ord('a')
    for c in string:
        result[ord(c) - base] += 1
    return result

a = input()
b = input()

cnt_a = cnt_alpha(a)
cnt_b = cnt_alpha(b)

ans = 0
for i in range(26):
    ans += abs(cnt_a[i] - cnt_b[i])
    
print(ans)
