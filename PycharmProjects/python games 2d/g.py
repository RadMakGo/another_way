def papa():

    print('type 1 to see what the biggest number and 2 to see the smalest number')
    y = input('type here:')

    if y == '1':
        a = int((input('first number')))
        b = int((input('second number')))
        c = int((input('third number')))
        m = a
    if a > b and a > c:
        m = a
        print('the biggest number is' + str(m))


    elif b > c:
        m = b
        print('the biggest number is' + str(m))


    else:
        m = c
        print('the biggest number is' + str(m))





















