n = int(input())

count = 0
num = 666

while True:
    if "666" in str(num):
        count = count + 1
        if count == n:
            print(num)
            break
    num = num + 1
