def f(a):
    if a == 0:
        return 1
    else:
        return a * f(a - 1)

x, n = int(input()), int(input())
if n >= 0:
    print(x ** n / f(n))
else:
    print('The factorial of the negative part cannot be subtracted')