
# 1. To make parameter optional.
# 2. Assign value to parameter in function definidion.
# 3. If we pass value to default para, it takes passed value
#    If we don't pass value to defalult para, it takes defalult value.
# 4. Flow from right to left (why - positional parameter concept)



def emp(id, name, sal=20000, dept='Backoffice'):
    print('ID:',id)
    print('Name:',name)
    print('Salary:',sal)
    print('DEPARTMENT:',dept)

emp(101, 'Abasd')
emp(102, 'abad', 50000)
emp(103,'XYZ', 40000,'IT')