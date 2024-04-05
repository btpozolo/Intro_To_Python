#1
people = ['Blake', 'Giulia', 'Michael', 'Lauren',]
print(len(people))

#2
stuff = ('hello', 'world', 'bye', 'now')
helper_list = list(stuff)
helper_list[2] = 'goodbye'
stuff = tuple(helper_list)
print(stuff)

#3
"""
Differences: 
    Tuples: unmutable, initialized through ()
    Lists: mutable, initialized through []
Similarities:
    Tuples and Lists are: both collections, both convert strings into individual characters 

"""

#4
"""
We can treat strings as sequences because each individual character in the string is an ordered object
"""

#5
"""
Set types differ from the sequence type as sequences are ordered and can be called with specific indices,
sets are unordered and cannot be called by specific positions
"""

#6
pi = 3.141592
str_pi = str(pi)
print(str_pi)
type(str_pi)

#7
range(7)            # 0 1 2 3 4 5 6
range(1, 6)         # 1 2 3 4 5
range(3, 15, 4)     # 3 7 11 14
range(3, 8, -1)     # 
range(8, 3, -1)     # 8 7 6 5 4

#8
range_1 = range(3, 17, 4)
print(tuple(range_1))

#9
my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)

"""
1)  they are equal
2)  they are not the same object
3)  yes, they are equal
4)  yes, they are the same object
"""

#10
names = { 'Chris', 'Clare', 'Karis', 'Karl',
          'Max', 'Nick', 'Victor' }
print(names)
"""
This code will not print in alphabetical order as it is a set, will print random order
"""

#11
my_dict = {
    'Alice' :       'USA',
    'Francois' :    'Canada',
    'Inti' :        'Peru',
    'Monika' :      'Germany',
    'Sanyu' :       'Uganda',
    'Yoshitaka' :   'Japan',
}
type(my_dict)
print(my_dict['Inti'])