a = input('Введите строку: ')
s = a.split()
s1 = []
s2 = []
for i in range(len(s)):
    if s[i][-1].lower() == 'я':
        s1.append(s[i])
    if s[i][0].lower() == 'а':
        s2.append(s[i])
print(f'Начинаются на букву "А":{' '.join(s2)}')
print(f'Кончается на букву "Я":{' '.join(s1)}')