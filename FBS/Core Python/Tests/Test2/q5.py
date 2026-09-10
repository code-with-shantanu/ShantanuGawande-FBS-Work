p1 = int(input('Enter price of first product'))
p2 = int(input('Enter price of second product'))
p3 = int(input('Enter price of third product'))
p4 = int(input('Enter price of fourth product'))
p5 = int(input('Enter price of fifth product'))

t1 = (p1+p2+p3+p4+p5)*0.18
t2 = p1+p2+p3+p4+p5

t = t1 + t2

print('Total cost',t)