num = int(input("Enter a number:"))

n1 = num // 2000
num = num % 2000

n2 = num // 500
num = num % 500

n3 = num // 200
num = num % 200

n4 = num // 100
num = num % 100

n5 = num // 50
num = num % 50

n6 = num // 20
num = num % 20

n7 = num // 10
num = num % 10

total= n1+n2+n3+n4+n5+n6+n7

print("Total number of notes:",total )