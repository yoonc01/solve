import sys

input = sys.stdin.readline

def fact(n):
    ans = 1
    for i in range(2, n + 1):
        ans = ans * i
    return ans

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    print(fact(m) // (fact(n) * fact(m - n)))