#num = 235
num = int(input('Enter number to separate:'))
while(num>0):
    d = num % 10
    print(d)
    num = num // 10