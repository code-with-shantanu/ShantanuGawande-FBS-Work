#### Numeric
#1. int
var = 10

#2. float 
var = 3.14

#3. complex
var = 10 + 5j #real + imaginary

print(type(var))

### Text
var = 'Firstbit Solution'
var = "Firstbit's Solution"
var = '''
This is first line. 
This is second line.
'''
var = """
This is first line. 
This is second line.
"""

print(type(var))


### Sequential
#1. list
var = [10, 20, 30, 40]

#2. tupple
var = (10, 20, 30, 40)

#3. range
var = range(1, 20)

print(type(var))

### Set type
#1. set
var = {10, 20, 30, 40}

#2. frozenset
var = frozenset({10, 20, 30, 40,})

print(type(var))

### Mapping
#1. dict
var = {1:'Python', 2:' Java', 3:'c'}
print(type(var))


### Other
#1. boolean
var = True 

#2. Nonetype
var = None

print(type(var))
