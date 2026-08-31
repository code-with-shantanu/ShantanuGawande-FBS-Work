p = int(input("Enter principle interest:"))
t = int(input("Enter time:"))
r = int(input("Enter rate of interest:"))

a = (1+r/100) **t
ci = (a*p)-p

print("Coumpound interest is:",ci)