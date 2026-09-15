n = int(input('enter number: '))
fact = 1
sum = 0
for i in range(1,n+1):
    fact *= i
    sum += (i)/fact
    print(fact)

print('sum',sum)