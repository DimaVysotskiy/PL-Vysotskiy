flag = False

while flag == False:
    try:
        #input
        n = int(input('Enter the quantity of row:'))
        m = int(input('Enter the quantity of items in row:'))
        print()

        # if enter only one row
        if n == 1:
            print('Enter more than one row. This operation meaningless.')
            print()

        # if input < 0
        elif n <= 0 or m <= 0:
            print('Enter value > 0')
            print()

        else:
            #generation matrix
            a = []
            for i in range(n):
                b = []
                for j in range(m):
                    #input in matrix
                    x = int(input(f'Enter item from matrix in position[{i}][{j}]:'))
                    b.append(x)
                a.append(b)
            print('~' * m * 2)

            #matrix output(unprocessed)
            for row in a:
                print(*row)
            print('~' * m * 2)

            #matrix processing
            for i in range(n - 1):
                for j in range(m):
                    a[i][j] -= a[n - 1][j]

            # matrix output(processed)
            for row in a:
                print(*row)
            print('~' * m * 2)

            #for try-except block
            flag = True
            print('End')

    except ValueError:
        print()
        print('Input error! Enter only integers!', )
        print('/////////////////////////////////')
        print()