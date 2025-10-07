n = int(input())

is_exist = False
for i in range(n):
    string_i = str(i)
    sum_val = i
    for num in string_i:
        sum_val = sum_val + int(num)
        
    if sum_val == n:
        print(i)
        is_exist = True
        break

if not is_exist:
    print(0)