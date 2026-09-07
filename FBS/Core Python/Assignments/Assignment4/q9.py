n = int(input('Enter a number for range:'))
d = int(input('Enter a divisor:'))

for i in range (1,n+1):
    if (i % d == 0 ):
        print(i, end=',')