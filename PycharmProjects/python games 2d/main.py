a = int((input('first number')))
b = int((input('second number')))
c = int((input('third number')))
m = a
if a < b and a < c:
    m = a
elif b < c:
    m = b
else:
    m = c

print('the lowest number is ' + str(m) )
