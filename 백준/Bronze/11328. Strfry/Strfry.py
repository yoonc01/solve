import sys
input = sys.stdin.readline

n = int(input())
base = ord('a')

for _ in range(n):
    s1, s2 = input().split()

    if len(s1) != len(s2):
        print("Impossible")
        continue

    cnt1 = [0] * 26
    cnt2 = [0] * 26

    for c1, c2 in zip(s1, s2):
        cnt1[ord(c1) - base] += 1
        cnt2[ord(c2) - base] += 1

    print("Possible" if cnt1 == cnt2 else "Impossible")