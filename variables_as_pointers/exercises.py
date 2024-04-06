#1
"""
line one compares equivalence, ie do they output the same result
line two checks if they are referencing the same object
"""

#2



set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

"""
This will print, <set> {42, 'Monthy Python', ('a', 'b', 'c'), range(5,10)}
"""

#3
dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict1
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])
"""
'Holy Grail' - wrong dict() call creates a new object
"""

#4
#will return 42 as this shallow copy still points to the same nested objects

#5
# You may modify this line
from copy import deepcopy


dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = deepcopy(dict1) #

# All of these should print False
print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])

#
# All of these should print True

print(dict1['a'][0][0] is dict2['a'][0][0])
print(dict1['a'][0][1] is dict2['a'][0][1])
print(dict1['a'][1][0] is dict2['a'][1][0])
print(dict1['a'][1][1] is dict2['a'][1][1])
print(dict1['b'][0][0] is dict2['b'][0][0])
print(dict1['b'][0][1] is dict2['b'][0][1])
print(dict1['b'][1][0] is dict2['b'][1][0])
print(dict1['b'][1][1] is dict2['b'][1][1])

#7
dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1)

print(dict1         is dict2)               # false
print(dict1['a']    is dict2['a'])          # false
print(dict1['a'][0] is dict2['a'][0])       # true
print(dict1['a'][1] is dict2['a'][1])       # true
print(dict1['b']    is dict2['b'])          # false
print(dict1['b'][0] is dict2['b'][0])       # true
print(dict1['b'][1] is dict2['b'][1])       # true
