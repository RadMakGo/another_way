hoursr = int(input('type hours'))
minuter = int(input('type min'))

hourss = int(input('type hours'))
minutes = int(input('type min'))
if hoursr > hourss:
    print('YOU TOO LATE')
elif hourss == hoursr and minuter > minutes:
    print('YOY TOO LATE')

else:
    print('GOOD JOB')
