while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break

    sides = sorted([a, b, c])

    if sides[2] >= sides[0] + sides[1]:
        print("Invalid")

    elif a == b == c:
        print("Equilateral")

    elif a == b or b == c or a == c:
        print("Isosceles")

    else:
        print("Scalene")
