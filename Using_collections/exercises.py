#1
my_list = list(range(0, 25, 3))
print(my_list[6])

#2
seq = 'Launch School'
print(seq[seq.find('c'): seq.find('c') + 6])

#3
tup = (1, 2, 3, 4, 5,)
rev_tup = tuple(reversed(tup))
print(rev_tup[1:-1])

#Alternative method
rev_tup = tup[-2:0:-1]
print(rev_tup)

#4
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}
print(pets['Dog'])
print(pets.get('Lizard'))   # get allows to specify error handling
print(pets.get('Lizard', '<silence>'))

#5
'cat'                       # can be a key
(3, 1, 4, 1, 5, 9, 2)       # can be a key
['a', 'b']                  # can't be a key
{'a': 1, 'b': 2}            # can't be a key
range(5)                    # can be a key
{1, 4, 9, 16, 25}           # can't be a key
3                           # can be a key
0.0                         # can be a key
frozenset({1, 4, 9, 16, 25})    # can be a key

#6
print('abc-def'.isalpha())      # False
print('abc_def'.isalpha())      # False
print('abc def'.isalpha())      # True
print('abc def'.isalpha() and   # False
      'abc def'.isspace())      
print('abc def'.isalpha() or    # True
      'abc def'.isspace())
print('abcdef'.isalpha())       # True
print('31415'.isdigit())        # True
print('-31415'.isdigit())       # False
print('31_415'.isdigit())       # False
print('3.1415'.isdigit())       # False
print(''.isspace())             # False

#7
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

info_updated = info.split(':')
print(info_updated)
info = '+'.join(info_updated)
print(info)

info.replace(':', '+')

#8 
"""
This code is different as #1 slices string into substring and then returns index
within that substring. #2 however keeps ths string intact and returns the index 
acros the full string
"""

#9
stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][3] = 606
print(stuff)

#10
cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

print(cats['Pete']['Cocoa']['enjoys'])

#11
print('johnson' in 'Joe Johnson')           # false
print('sen' not in 'Joe Johnson')           # true
print('Joe J' in 'Joe Johnson')             # true
print(5 in range(5))                        # false
print(5 in range(6))                        # true
print(5 not in range(5, 10))                # false
print(0 in range(10, 0, -1))                # false
print(4 in {6, 5, 4, 3, 2, 1})              # true
print({1, 2, 3} in {1, 2, 3})               # true - wrong need to review. sets only check if value is in set
print({3, 2} in {1, frozenset({2, 3})})     # true

#12
numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

print(3 in numbers1)

#13
cats = ('Cocoa', 'Cheddar',                 
        'Pudding', 'Butterscotch')
print('Butterscotch' in cats)               # True
print('Butter' in cats)                     # False - searches complete match
print('Butter' in cats[3])                  # True
print('cheddar' in cats)                    # False - case sensitive

#14
my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

tup_list = zip(my_str, my_list, my_tuple, my_range)
print(list(tup_list))

#15
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

keys = pets.keys()
del pets['Dog']
pets['Snake'] = 'Sssss'
print(keys)                 # Cat, Dog, Bird - wrong keys update variables pointing to them as updated