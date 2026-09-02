g = input('Enter Gender(M or F):')
a = int(input('Enter Age:'))

if g == 'm':
    if a >= 21:
        print('Eligible to Marry')
    else:
        print('Not Eligible to Marry')
else:
    if a >=18:
        print('Eligible to Marry')
    else:
        print('Not Eligible to Marry')

