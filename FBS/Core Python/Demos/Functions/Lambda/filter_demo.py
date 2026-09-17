data= [1,2,3,4,5,6,7,8,9,10]

res = tuple(filter(lambda num: num*num, data))
print(res)

res = tuple(filter(lambda num: num%2 ==0, data))
print(res)