w = 8
a = float(input("Enter area of one wall: "))

i = float(input("Enter interior painting cost: "))
e = float(input("Enter exterior painting cost: "))

area = a * w

c_i = area * i
c_e = area * e

total = c_i + c_e

print(f'Total cost of painting is:{total}')