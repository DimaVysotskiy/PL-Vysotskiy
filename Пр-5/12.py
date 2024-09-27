a = input("Введите строку: ")
s = a.split()
for i in range(len(s)):
    if s[i][-1].lower() == 'я':
        print(s[i], end=' ')