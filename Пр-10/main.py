with open('VysotskiyD.V._UB41_vvod.txt') as vvod:
    s = vvod.readlines()
    q_row = len(s)#q - quantity

    # create matrix + del '\n' in items in matrix
    a = []
    for i in range(q_row):
        if i != q_row - 1:#['***'] ---> ['*', '*', '*'] for the operation processing matrix
            b = []
            b.extend(s[i][:-1])
            a.append(b)
        else:
            b = []
            b.extend(s[i])
            a.append(b)

    #processing matrix
    for i in range(q_row):
        for j in range(q_row):
            if i == j:
                a[i][j] = '+'
            else:
                a[i][j] = '-'

with open('VysotskiyD.V._UB41_vivod.txt', '+r') as vivod:
    for i in range(len(a)):
        row = ''.join(a[i])
        vivod.write(row + '\n')#write - del text in file and add new text