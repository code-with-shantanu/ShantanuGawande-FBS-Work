l = int(input('Enter length of rectangle:'))
b = int(input('Enter breadth of triangle:'))
r = int(input('Enter radius of circle:'))

a1 = l*b
a2 = (3.14 * r**2) / 2

a = a1 + a2 

print (f'Are of given diagram is:{a}')

p1 = 2 * (l+b)
p2 = 2 * 3.14 * r

p = p1+p2

print (f'Perimeter of given diagram is:{p}')