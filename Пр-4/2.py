a, b = int(input()), int(input())
if a < b:
    print(*list(i for i in range(a, b + 1)))
else:
    print(*list(x for x in range(a, b - 1, -1)))