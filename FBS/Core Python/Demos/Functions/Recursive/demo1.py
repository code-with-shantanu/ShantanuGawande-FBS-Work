# def series(n):
#     if n>0:
#         print(n)
#         series(n-1)

# series(5)


def series(n):
    sum = 0
    if n>0:
        sum += n
        series(n-1)
    print(sum)

n=5
series()
