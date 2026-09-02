a1 = int(input("Enter age of person 1: "))
a2 = int(input("Enter age of person 2: "))
a3 = int(input("Enter age of person 3: "))
a4 = int(input("Enter age of person 4: "))
a5 = int(input("Enter age of person 5: "))

price = float(input('Enter price per person:'))

if a1 < 12:
    a1 = price - (price * 0.30)
elif a1 > 59:
    a1 = price - (price * 0.50)
else:
    a1 = price

if a2 < 12:
    a2 = price - (price * 0.30)
elif a2 > 59:
    a2 = price - (price * 0.50)
else:
    a2 = price

if a3 < 12:
    a3 = price - (price * 0.30)
elif a3 > 59:
    a3 = price - (price * 0.50)
else:
    a3 = price

if a4 < 12:
    a4 = price - (price * 0.30)
elif a4 > 59:
    a4 = price - (price * 0.50)
else:
    amount4 = price

if a5 < 12:
    a5 = price - (price * 0.30)
elif a5 > 59:
    a5 = price - (price * 0.50)
else:
    a5 = price

total = a1 + a2 + a3 + a4 + a5

print("Total ticket amount for all 5 people:", total)