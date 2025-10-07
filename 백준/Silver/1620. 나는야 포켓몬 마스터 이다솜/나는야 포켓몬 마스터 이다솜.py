n, m = map(int, input().split())

d = {}
for i in range(1, n + 1):
    name = input()
    d[name] = i
    d[str(i)] = name
    
for _ in range(m):
    print(d[input()])