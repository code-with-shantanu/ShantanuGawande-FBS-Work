n = int(input('Enter three digit number:'))

d1 = n % 10
n = n // 10
d2 = n % 10
n = n // 10
d3 = n 


if d1 == d2 * 4  and d3 == d2 * 2: 
    print('Yes, you have done it')
else:
    print('Please try next time')
