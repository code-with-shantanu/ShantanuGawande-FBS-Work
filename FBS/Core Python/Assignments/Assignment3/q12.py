n = int(input('Enter a three digit number:'))

num = n
d1 = n % 10 
n = n//10

d2 = n % 10
n = n//10

d3 = n % 10

temp = d1*100 + d2*10 + d3
print(temp)
if temp == num:
    print('Given Number is Palindrome')
else:
    print('Given Number is Not Palindrome')
