def selectionSort(li):
    size = len(li)
    for i in range(0, size-1):
        min_ind = 1
        for j in range(i + 1, size):
            if(li[j] < li[min_ind]):
                min_ind = j 
        li[i], li[min_ind] = li[min_ind], li[i]

li= [10, 40, 50, 60, 30, 20]
print(li)
selectionSort(li)
print(li)
