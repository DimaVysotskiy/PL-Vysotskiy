def f12_1(s):
    a = [i for i in s if i % 2 != 0]
    return min(a)


def f12_2(a, b):
    c = a
    a = b
    b = c
    return a, b

print(f12_1([2, -4, 6, 7, -100, -9, 6]))
print(f12_2([1, 2, 3], [0, 9, 8]))
