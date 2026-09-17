def addition(*num):
    sum = 0 
    for val in num:
        sum += val
    return sum

res = addition(10,20,30,40,50)
print(res)
    