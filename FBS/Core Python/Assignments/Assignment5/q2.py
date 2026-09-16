n = int(input("Enter number of students: "))

total_percentage = 0

for i in range(n):
    print("Student", i + 1)

    total = 0

    for j in range(5):
        marks = float(input("Enter marks of subject " + str(j + 1) + ": "))
        total = total + marks

    percentage = total / 5

    print("Percentage =", percentage, "%")

    total_percentage = total_percentage + percentage

average = total_percentage / n

print("Average Percentage =", average, "%")
