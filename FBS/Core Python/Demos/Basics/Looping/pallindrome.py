num = int(input('Enter a number:'))
temp = num
rev_num = 0

while (temp > 0):
    d = temp % 10
    temp = temp // 10
    rev_num = rev_num *10 + d
print(rev_num)

if (num == rev_num):
    print('Number is Pallindrome number')
else:
    print('Number is not Pallindrome number')

    