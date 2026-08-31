days = int(input('Enter no. of days:'))

y = days // 365
w = (days % 365) // 7
d = w % 7

print(f'Years:{y}, Weeks:{w}, Days:{d}')