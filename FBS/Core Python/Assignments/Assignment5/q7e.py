x = float(input("Enter value of x: "))
n = int(input("Enter number of terms: "))

sum = 0
d = 1

for i in range(1, n + 1):

    term = (x ** i) / d

    if i % 2 == 0:
        sum = sum - term
    else:
        sum = sum + term

    d = d + 2

print("Sum =", sum)
