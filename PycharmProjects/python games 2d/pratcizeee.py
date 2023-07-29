
y = print(input('type 1 to find biggest number and type 2 to find smallest number:'))

if y == '1':
        a = int((input('first number')))
        b = int((input('second number')))
        c = int((input('third number')))
        d = a
        if a > b or a > c:
            d = a

        elif b > c:
            d = b

        else:
            d = c

        print('the lowest number is' + str(d))

















