def checkstrongnumber(num):
    original = num
    s = 0
    n = len(str(num))
    while num > 0:
        d = num % 10
        num = num // 10
        s = s + d ** n

    if s == original:
        print('Strong Number')
    else:
        print('Not Strong Number')

checkstrongnumber(1634)
