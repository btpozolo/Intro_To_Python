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

#2
