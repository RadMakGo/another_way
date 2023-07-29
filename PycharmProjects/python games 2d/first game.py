import random
streak = 0
number = random.randint(1, 5)
print('hello what your name')
myname = input("please type your name")
print('are you ready to play  you should guees 1 to 5 numbers')
while streak < 2:
    guess = int(input())

    streak += 1

    if guess < number:
        print('my number is bigger')
    if guess > number:
        print('my number is lower"')
    if guess ==number:
        break

if guess == number:
    streak = str(streak)
    print(myname +  ' won '  +  streak)

if guess != number:
    number = str(number)
    print('you lose the number was ' +  number )