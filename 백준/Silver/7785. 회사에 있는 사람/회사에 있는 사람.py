n = int(input())

entered = set()

for _ in range(n):
    name, state = input().split()
    if state == "enter":
        entered.add(name)
    else:
        entered.remove(name)
        
ans = sorted(entered, reverse=True)

print("\n".join(ans))