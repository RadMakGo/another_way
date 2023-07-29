def caculator():
    num1 = int(input('first number'))
    num2 =int(input('second  number'))
    operation = input("type which math function you want to do? you can do: devision multiply plus minus type here: " )
    if operation == '+':
        print('{} + {} ='.format(num1, num2), num1 + num2)
    elif operation == '-':
        print('{} - {} ='.format(num1, num2), num1 - num2)
    elif operation == '*':
        print('{} * {} ='.format(num1, num2), num1 * num2)
    elif operation == "/":
        print('{} / {} ='.format(num1, num2), num1 / num2)
    else:
        print('something went wrong :/')
    again()

def again():
    again22 = input('do you want to resolve the math problem? type yes if you want resolve type no if you dont want to resolve')
    if again22 == 'yes':
        caculator()
    elif again22 == 'no':
        print('goodbye :)')
    else:
        print("something went wrong")
        again()


caculator()

