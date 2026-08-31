import random

r = random.randint(1000,10000) 

uid = int(input('Enter valid userid:'))
password = input('Enter valid password')

if (uid == 1234 and password == 's1234'):
    syscap = r
    print(f'captcha is:{r}')
    captcha = int(input('Enter captcha '))
    if (captcha == syscap):
        print('Valid user')
    else:
        print('Invalid Captcha')
else:
    print('Invalid user')
