n = int(input("Enter number of employees: "))
total = 0

for i in range(n):
    basic = int(input("Enter basic salary: "))

    if basic < 20000:
        da = basic * 10 / 100
        ta = basic * 12 / 100
        hra = basic * 15 / 100
    else:
        da = basic * 15 / 100
        ta = basic * 18 / 100
        hra = basic * 20 / 100

    salary = basic + da + ta + hra
    print("Total salary =", salary)

    total = total + salary

print("Total salary of all employees =", total)
