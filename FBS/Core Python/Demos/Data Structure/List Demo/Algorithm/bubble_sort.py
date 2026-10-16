def bubblesort(li):
    size = len(li)
    for i in range(1, size):
        for j in range(1, size-i):
            if (li[j] > li[j+1]):
                li[j] ,li[j+1] = li[j+1] ,li[j]

li = [10, 30, 40, 50, 20, 40]

bubblesort(li)
print(li)