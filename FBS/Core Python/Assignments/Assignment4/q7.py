n = int(input('Enter a number:'))

for i in range (n+1):
    if (i % 2 != 0  and i % 3 != 0):
        print(i, end=',')