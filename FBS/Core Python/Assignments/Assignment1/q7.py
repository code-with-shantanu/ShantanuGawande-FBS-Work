import math

a = int(input("Enter first constant:"))
b = int(input("Enter second constant:"))
c = int(input("Enter third constant:"))

r = math.sqrt(b**2 - 4*a*c)

x1 = (-b + r)/ (2*a) 
x2 = (-b - r)/ (2*a)

print("Roots of this eqation are:",x1,"&",x2)

print("Roots of this eqation are:",x1.real,"&",x2.real)
