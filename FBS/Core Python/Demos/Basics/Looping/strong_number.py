num = int(input('Enter a number:'))
temp = num
sum = 0

while (temp > 0):
    d = temp % 10
    temp = temp // 10
    fact = 1
    for i in range (1, d+1):
        fact = fact * i
    sum = sum + fact
print()

if (num == sum):
    print('Number is Strong number')
else:
    print('Number is not Strong number')

    