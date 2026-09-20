# c. 1^1 + 2^2 + 3^3+ ...... n^n

def sumOfSeries(n):
    s = 0
    v = 1
    for i in range(1,n+1):
        v = i ** i
        s = s + v

    print(s)

sumOfSeries(4)
    