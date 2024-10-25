def f(a, b, c):
    ma = 0.5 * (2 * (b ** 2 + c ** 2) - a ** 2) ** 0.5
    mb = 0.5 * (2 * (a ** 2 + c ** 2) - b ** 2) ** 0.5
    mc = 0.5 * (2 * (b ** 2 + a ** 2) - c ** 2) ** 0.5
    a1 = 0.5 * (2 * (mb ** 2 + mc ** 2) - ma ** 2) ** 0.5
    b1 = 0.5 * (2 * (mb ** 2 + mc ** 2) - ma ** 2) ** 0.5
    c1 = 0.5 * (2 * (mb ** 2 + mc ** 2) - ma ** 2) ** 0.5
    return print(a1, b1, c1)

x, y, z = int(input()), int(input()), int(input())
f(x, y, z)

# def f(s):
#     a, b, c = s[0], s[1], s[2]
#     ma = 0.5 * (2 * (b ** 2 + c ** 2) - a ** 2) ** 0.5
#     mb = 0.5 * (2 * (a ** 2 + c ** 2) - b ** 2) ** 0.5
#     mc = 0.5 * (2 * (b ** 2 + a ** 2) - c ** 2) ** 0.5
#     return [ma, mb, mc]
#
# x, y, z = int(input()), int(input()), int(input())
# s1 = [x, y, z]
# q = f(s1)
# print(*f(q))