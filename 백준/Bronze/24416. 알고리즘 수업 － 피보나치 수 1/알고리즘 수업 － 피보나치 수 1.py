n = int(input())

ans = [0, n - 2]

def fib1(n):
    if n == 1 or n == 2:
        ans[0] = ans[0] + 1
        return 1
    return fib1(n - 1) + fib1(n - 2)

fib1(n)
print(*ans)