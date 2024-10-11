def f(n):
    for x in range(1, n - 1):
        for y in range(x + 1, n):
            cx = 0
            cy = 0
            for j in range(1, y // 2 + 1):
                if cx > y or cy > x:
                    break
                if x % j == 0 and x > j:
                    cx += j
                if y % j == 0:
                    cy += j
            if cx == y and cy == x:
                print(x, y)

n = int(input()) #спросить о скорости выполнения
f(n)
