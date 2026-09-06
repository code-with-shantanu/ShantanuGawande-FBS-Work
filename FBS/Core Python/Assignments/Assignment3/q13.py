u = float(input("Enter total electricity units consumed: "))

if u <= 50:
    bill = u * 0.50
elif u <= 150:  # first 50 + next 100
    bill = 50 * 0.50 + (u - 50) * 0.75
elif u <= 250:  # first 150 + next 100
    bill = 50 * 0.50 + 100 * 0.75 + (u - 150) * 1.20
else:  # above 250
    bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (u - 250) * 1.50

s = bill * 0.20
total = bill + s


print(f"Total electricity bill: Rs. {total}")