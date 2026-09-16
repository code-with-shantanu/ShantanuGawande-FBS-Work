n = int(input("Enter number of terms: "))

term = 1
sum = 0

for i in range(n):
    sum = sum + term
    term = term * 2

print("Sum =", sum)
