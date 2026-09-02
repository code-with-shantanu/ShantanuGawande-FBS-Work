s1 = int(input('Enter marks of first subject:'))
s2 = int(input('Enter marks of second subject:'))
s3 = int(input('Enter marks of third subject:'))
s4 = int(input('Enter marks of fourth subject:'))
s5 = int(input('Enter marks of fifth subject:'))

p = (s1+s2+s3+s4+s5)/5

if p > 90:
    print('Passed in First Class')
elif p > 75:
    print('Passed in Second Class')
elif p > 50:
    print('Passed in third Class')
elif p > 35:
    print('Passed in fourth Class')
else:
    print('Failed')
    
