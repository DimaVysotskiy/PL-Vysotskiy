def f():
    n = int(input())
    if n == 0:
        return 0
    else:
        return max([n, f()])

print(f())


# #processing output list from def f()
# def f1(a):
#     s = []
#     while type(a[-1]) is list:
#         s.append(a[0])
#         a = a[-1]
#     s.append(a[0])
#     return print(max(s))
#
# #def for input
# def f():
#     n = int(input())
#     if n == 0:
#         return 0
#     else:
#         return [n, f()]
#
# print(f1(f()))








