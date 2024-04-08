## Reading Documentation
#1 

string = "Ahola, World!"
print(string.lower().rjust(40))

rev_string = string[::-1]
print(rev_string)

fruits = ["apple", "banana", "cherry", "peach", "watermelon"]
fruits.index('cherry')

## Conditionals
#2
import random
random_number = random.randint(0, 1)
if random_number == 1:
    print('Yes!')
else:
    print('No.')

print('Yes!' if random_number else 'No.')


weather = 'sunny'

if weather == 'sunny':
    print("It's a beautiful day!")
elif weather == 'rainy':
    print('Grab your umbrella.')
else:
    print("Let's stay inside")


match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print('Grab your umbrella.')
    case '_':
        print("Let's stay inside")

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

## Reading Documentation 2

name = "Victor"
profession = "programmer"

print('Hello, {name}. You are a {profession}.')
print(f'Hello, {name}. You are a {profession}.')

# 2

ice_cream_density = 10

while ice_cream_density > 0:
    print('Drip...')
    ice_cream_density -= 1

print('The ice cream melted.')

#3
4 * 5 + 3**2 / 10

"""
4 * 5 + 9 / 10
20 + 0.9
20.9
"""

#4
import datetime 

datetime.date.today()

current_time = datetime.datetime.now()
print(current_time)

#5 

from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]

sample = "blake"

sample.find('ak')

#7
tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet) + 5

## Loops
for num in range(0, 11, 2):
    print(num)

#2
for i in range(10, 0, -1):
    print(i)

#3
greeting = 'Aloha!'

for num in range(3):
    print(greeting)

#4
for num in range(1, 101):
    print(num * 2)

#5
lst = [1, 3, 7, 15]
index = 0

while index < len(lst):
    print(lst[index])
    index += 1

#6
friends = ['Sarah', 'John', 'Hannah', 'Dave']

for name in friends:
    print(f'Hello, {name}!')

#7
cities = ['Istanbul', 'Los Angeles', 'Tokyo', None,
          'Vienna', None, 'London', 'Beijing', None]

for city in cities:
    if city is None:
        continue

    print(f'{city} has a length of {len(city)}')

#8

while True:
    print("and on")
    break

#9
fish_list = ['Dory', 'Marlin', 'Gill', 'Nemo', 'Bruce']

for fish in fish_list:
    print(fish)
    if fish == 'Nemo':
        break

#10
while True:
    print('Should I stop looping?')
    answer = input() 
    if answer == 'yes':
        break

## Functions

#1
def multiply(num1, num2):
    return num1 * num2

multiply(12, 4)

#2
def bruce_eckel_quote():
    print('Python is exectuable pseudocode.')

bruce_eckel_quote()

#3
def cite(str1, str2):
    print(f'{str1} said: "{str2}"')

cite('Bruce Eckel', 'Python is executable pseudocode.')
# Bruce Eckel said: "Python is executable pseudocode."

#4
def squared_number(number):
    return number ** 2

squared_number(3)   # 9

#5

def multiples_of_three():
    divisor = 1

    for dividend in range(3, 31, 3):
        print(f'{dividend} / {divisor} = 3')
        divisor += 1

multiples_of_three
"""
3 / 1 = 3
6 / 2 = 3
...
30 / 10 = 3
"""

#6
def compare_by_length(string_1, string_2):
    len_diff = len(string_1) - len(string_2)
    if len_diff == 0:
        return 0
    elif len_diff < 0:
        return -1 
    else:
        return 1
    

compare_by_length('patience', 'perseverance') # -1
compare_by_length('strength', 'dignity')      #  1
compare_by_length('humor', 'grace')           #  0

#7
string_1 = 'Captain Ruby'
string_1 = string_1.replace('Ruby', 'Python')
string_1

#8
def greet(country_code):
    match country_code:
        case 'en':
            return 'Hi!'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case _:
            return 'hello.'


print(greet('en'))         # Hi!
print(greet('fr'))         # Salut!
print(greet('pt'))         # Olá!
print(greet('de'))         # Hallo!
print(greet('sv'))         # Hej!
print(greet('af'))         # Haai!

#9
def extract_language(locale):
    return locale.split('_')[0]

print(extract_language('en_US.UTF-8'))      # en
print(extract_language('en_GB.UTF-8'))      # en
print(extract_language('ko_KR.UTF-16'))     # ko

def extract_region(locale):
    helper = locale.split('_')[1]
    return helper.split('.')[0]

print(extract_region('en_US.UTF-8'))    # US
print(extract_region('en_GB.UTF-8'))    # GB
print(extract_region('ko_KR.UTF-16'))   # KR

def local_greet(locale):
    language = extract_language(locale)
    region = extract_region(locale)

    match language:
        case 'en':
            match region:
                case 'US':
                    return 'Hey!'
                case 'GB':
                    return 'Hello!'
                case 'AU':
                    return 'Howdy'
        case 'fr':
            return 'Salut!'
        case 'pt':
            return 'Olá!'
        case 'de':
            return 'Hallo!'
        case _:
            return 'hello.'

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!

print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!

## Variable Scope
#1 error my_value not defined

#Strings
"These aren't the droids you're looking for.".__len__()

'confetti floating everywhere'.upper()

name = 'Roger'

'RoGeR'.casefold() == name.casefold()

rhyme = "A pirate I was meant to be!\nTrim the sails and roam the sea!"
print(rhyme)

char_sequence = 'TXkgaG92ZXJjcmFmdCBpcyBmdWxsIG9mIGVlbHMu'

'x' in char_sequence

def is_empty(string_1):
    return len(string_1) == 0

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True

def is_empty_or_blank(s):
    return not s.isalpha()

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

'launch school tech & talk'.title()


def starts_with(string, substring):
    for index in range(0, len(substring)):
        if string[index] != substring[index]:
            return False
    return True

def starts_with(string, substring):
    return string.startswith(substring)


print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

def count_substrings(string, substring):
    return string.count(substring)


print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0

## Lists
#1 
def first(list):
    if list:
        return list[0]
    else:
        return 'No elements in list'

print(first(['Earth', 'Moon', 'Mars']))  # Earth

test = []
first(test)

#2
def last(list):
    if list:
        return list[-1]
    else:
        return 'No elements in list'
    
print(last(['Earth', 'Moon', 'Mars']))  # Mars

#3
energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']
energy.remove('fossil')
energy.append('geothermal')

energy

#4
alphabet = 'abcdefghijklmnopqrstuvwxyz'
letters = []
for letter in alphabet:
    letters.append(letter)

list(alphabet)
letters

scores = [96, 47, 113, 89, 100, 102]
len([score for score in scores if score >= 100])

vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

for groups in vocabulary:
    for word in groups:
        print(word)


for outer_index in range(0, len(vocabulary)):
    for inner_index in range(0, len(vocabulary[outer_index])):
        print(vocabulary[outer_index][inner_index])

# happy
# cheerful
# merry
# glad
# tired
# sleepy
# etc...


some_value1 = [0, 1, 0, 0, 1]
some_value2 = 'I leave you my Kingdom, take good care of it.'

type(some_value1)
type(some_value2)


destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(city, places):
    for spot in places:
        if spot == city:
            return True
    return False

contains('Barcelona', destinations)  # True
contains('Nashville', destinations)  # False

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

# Write some code here.
print("-".join(passcode))
# Expected return value: '11-jZ5-hQ3f*-8!7g3-p3Fs'

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

while grocery_list:
    print(grocery_list.pop(0))

print(grocery_list)

## Dictionaries
#1

car = {
    'type' : 'sedan',
    'color' : 'blue',
    'mileage' : 80_000,
}

car['year'] = 2003

#3
car.pop('mileage')
del car['mileage'] # doesnt return value of pair
car

#4
print(car['color'])

#5
print(len(car))

#6
student = {
    'id': 123,
    'grade': 'B',
}

'name' in student
'grade' in student

#7
cars = {
    'car' : {
        'type': 'sedan',
        'color' : 'blue',
        'year': 2003

    },
    'truck' : {
        'type': 'pickup',
        'color': 'red',
        'year': 1998

    }
}

car = [
    ['type', 'sedan'],
    ['color', 'blue'],
    ['year', 2003]
]



numbers = {
    'high':   100,
    'medium': 50,
    'low':    25,
}

half_numbers = []

for num in numbers.values():
    half_numbers.append(num // 2)

print(half_numbers)

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

for num in numbers.items():
    print(f'A {num[0]} number is {num[1]}')

## Debugging
#1
def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among([0, 0, 1, 0, 2, 0])
find_first_nonzero_among(1)

#2
def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = input()

print(f"The result is {multiply_by_five(number)}!")

pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

pets['dog'].append('bowser') 

print(pets)  # Output: {'cat': 'pepe', 'dog': 'bowser', 'fish': 'oscar'}

info = {'name': 'Srdjan', 'age': 38}

print(info.get('city', 'Unknown'))

import copy

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(copy.deepcopy(sub_list))

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]


def find_maximum(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

print(find_maximum([45, 3, 10, 98, 22]))  # Expected 98
print(find_maximum([-1, 0, 5, 3]))         # Expected 5
print(find_maximum([-10, -3, -20, -2]))   # Expected -2

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0