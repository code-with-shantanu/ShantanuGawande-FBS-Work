def sumOfPrimenumbers(n):
    s = 0
    for i in range(2, n+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            s = s + i
            
    print(s)

sumOfPrimenumbers(5)
