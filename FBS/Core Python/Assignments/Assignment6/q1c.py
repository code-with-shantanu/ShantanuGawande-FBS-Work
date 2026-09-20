n = 5  # number of rows

for i in range(4):
    print(" " * (n - i), end="")  # leading spaces for alignment
    val = 1
    for j in range(i + 1):
        print(val, end=" ")
        val = val * (i - j) // (j + 1)
    print()