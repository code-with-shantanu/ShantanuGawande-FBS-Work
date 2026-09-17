# 1. To neglect positional para concept.
# 2. Assign value to parameter in function call.
# 3. Name of parameter in functional definition and function call should be same.
# 4. Flow from right to left(why- positional para flow left to right)


def emp(id, name, sal=20000, dept='Backoffice'):
    print('ID:',id)
    print('Name:',name)
    print('Salary:',sal)
    print('DEPARTMENT:',dept)

emp(name='abc', id=123, sal= 30000, dept='IT')
