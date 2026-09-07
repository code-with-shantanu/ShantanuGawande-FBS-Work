n = int(input('Enter a number:'))

for i in range (2, n+1):
    if (n % i == 0):
        print('Number is not prime number')
        break
else:
    print('Prime Number')
