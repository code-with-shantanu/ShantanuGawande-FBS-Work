def sumofdigits(num):
    s = 0
    while num > 0:
        d = num % 10
        num = num // 10
        s = s + d 

    print(s)

sumofdigits(129)
