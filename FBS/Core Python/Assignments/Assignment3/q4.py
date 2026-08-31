s1= int(input("Enter longest side of triangle:"))
s2= int(input("Enter second side of triangle:"))
s3= int(input("Enter third side of triangle:"))

s = s2+s3

if s1>0 and s2>0 and s3>0 and (s > s1):
    print ("Triangle is Valid")
else:
    print("Triangle is Invalid")

