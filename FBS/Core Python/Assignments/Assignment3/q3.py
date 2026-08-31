a1= int(input("Enter first angle of triangle:"))
a2= int(input("Enter second angle of triangle"))
a3= int(input("Enter thirst angle of triangle"))

if a1 and a2 and a3 >0 and a1+a2+a3 == 180 :
    print ("Triangle is Valid")
else:
    print("Triangle is Invalid")