n = int(input("Enter number of passengers: "))
cost = float(input("Enter cost of one ticket: "))

total_amount = 0

for i in range(n):
    age = int(input("Enter age of passenger " + str(i + 1) + ": "))

    if age < 12:
        ticket = cost - (cost * 30 / 100)
    elif age > 59:
        ticket = cost - (cost * 50 / 100)
    else:
        ticket = cost

    print("Ticket amount =", ticket)

    total_amount = total_amount + ticket

print("\nTotal amount =", total_amount)
