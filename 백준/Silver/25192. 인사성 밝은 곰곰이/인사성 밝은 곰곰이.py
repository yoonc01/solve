import sys

input = sys.stdin.readline

imo = set()

n = int(input())
ans = 0
for i in range(n):
    name = input().strip()
    if name == "ENTER":
        ans = ans + len(imo)
        imo = set()
    else:
        imo.add(name)
ans = ans + len(imo)        
print(ans)