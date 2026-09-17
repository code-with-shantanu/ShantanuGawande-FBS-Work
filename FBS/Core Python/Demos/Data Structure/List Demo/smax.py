li = [10,30,50,90,80,70]

max = li[0]
smax = 0

for ind in range (1, len(li)):
    if (li[ind] > max):
        smax = max
        max = li[ind]

    elif (li[ind]> smax):
        smax  = li[ind]

print('Max:', max)
print('SMax:', smax)
