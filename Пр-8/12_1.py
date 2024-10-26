flag = False

while flag == False:
    try:
        #input
        k = int(input('Enter the quantity of items in row:'))
        k1 = int(input('Enter the quantity of row:'))
        print()

        # if input < 0
        if k <= 0 or k1 <= 0:
            print('Enter value > 0')
            print()
        else:
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
        print()
        print('Input error! Enter only integers!')
        print('/////////////////////////////////')
        print()