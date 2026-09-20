#b. 1!+ 2! + 3! + 4!+..... + n!

def sumOfSeries(n):
    s = 0
    f = 1
    for i in range(1,n+1):
        f = f * i
        s = s + f

    print(s)

sumOfSeries(4)