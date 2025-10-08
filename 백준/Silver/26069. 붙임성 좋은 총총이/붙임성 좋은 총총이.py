import sys

input = sys.stdin.readline

T = int(input())

dancing = set(["ChongChong"])

for _ in range(T):
    a, b = input().split()
    if a in dancing or b in dancing:
        dancing.add(a)
        dancing.add(b)
print(len(dancing))
