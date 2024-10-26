flag = False

while flag == False:
    try:
        #input
        k = int(input('Enter the quantity of items in row:'))
        k1 = int(input('Enter the quantity of row:'))
        print()

        #matrix generation
        a = []
        for i in range(k1):
            b = ['*'] * k
            a.append(b)

        #matrix output(unprocessed)
        for row in a:
            print(*row)
        print()

        #processing matrix
        for i in range(k1):
            for j in range(k):
                if i == j:
                    a[i][j] = '+'
                else:
                    a[i][j] = '-'

        #matrix output(processed)
        for row in a:
            print(*row)
        print()

        # for try-except block
        flag = True
        print('End')

    except ValueError:
        print('Input error! Enter only integers!', )
        print('/////////////////////////////////')
        print()