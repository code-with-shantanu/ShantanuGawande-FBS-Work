li = [10,20,30,40,50,60,70]
sum = 0

# 1. Method 1: Iteration value

for ele in li:
    sum += ele

print(sum)


# 2. Method 2: Indexing

for ind in range(0,len(li)):
    sum += (li[ind])

print(sum)

