li = [10,50,30,5,55,90,100]
h = li[0]
for ind in range(1,len(li)):
    if (li[ind] < h):
        h = li[ind] 

print(h)
