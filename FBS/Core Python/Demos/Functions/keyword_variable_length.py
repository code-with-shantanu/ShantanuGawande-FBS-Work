

def emp(**data):
    for key, val in data.items():
        print (key,':' ,val)

emp(id = 1234, name= 'ABC', sal = 25000, dept= 'IT')