li = [10,20,30,40,50,60,90,80]

# h = li[0]
# for i in li:
#     if i>h:
#         h = i 

# print(h)



h = li[0]
for ind in range(1,len(li)):
    if (li[ind] > h):
        h = li[ind] 
print(h)
