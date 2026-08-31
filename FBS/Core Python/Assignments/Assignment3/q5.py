s1= int(input("Enter first side of triangle:"))
s2= int(input("Enter second side of triangle:"))
s3= int(input("Enter third side of triangle:"))

if(s1==s2==s3):
    print('Triangle is Equilateral Triangle')
elif s1==s2 or s2==s3 or s1==s3 :
    print('Triangle is Isosceles Triangle')
else:
    print('Triangel is Scalene Triangle')