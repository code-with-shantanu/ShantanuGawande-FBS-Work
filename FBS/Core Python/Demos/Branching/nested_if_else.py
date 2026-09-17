gender = input("Enter gender(M/F):")
age = int(input("Enter age:"))

if(gender == 'F'):
    if(age>=18):
        print("Girl is eligible for marriage")
    else:
        print("Girl is not eligible for marriage")

else:
    if(age>=21):
        print("Boy is eligible for marriage")
    else:
        print("Padhai karle beta.")



### 2nd code


gender =    input('Enter Gender Male or Female: ')
age = int(input('Enter age:  '))


if  (gender=='male' or 'Male' and age >=  18 or gender=='female' or 'Female' and age >=21):
    print(f'{gender}, is elegible to marry')
else:
    print(f'{gender}, you are minor and not elegible to marry yet')
    