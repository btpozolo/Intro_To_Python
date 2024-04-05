#1 
"""
the counter is never incremented in the while loop so it will never be false
"""

#2
# This solution reduces the repetition by calling int
# once only.

age = int(input('How old are you? '))

print(f'You are {age} years old.')

for num in range(10,50,10):
    print(f'In {num} years, you will be {age + num} years old.')

#3
my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    print(my_list[index])
    index += 1

for item in my_list:
    print(item)

#4
my_list = [6, 3, 0, 11, 20, 4, 17]

index = 0
while index < len(my_list):
    if my_list[index] % 2 == 0:
        print(my_list[index])
    index += 1

for item in my_list:
    if item % 2 == 1:
        print(item)

#5
my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for group in my_list:
    for item in group:
        if item % 2 == 0:
            print(item)

#6
my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

new_list = []

for item in my_list:
    if item % 2 == 0:
        new_list.append('even')
    else:
        new_list.append('odd')

print(new_list)

#7
def find_integers(seq):
    ints = []
    for item in seq:
        if type(item) is int:
            ints.append(item)
    return ints

def find_integers(seq):
    return [item for item in seq if type(item) is int]

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]

#8
my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

result = {
    key : len(key) for key in my_set 
    if len(key) % 2 != 0 
}

print(result)

#9
def factorial(num):
    value = 1 
    for index in range(1,num + 1):
        value *= index
    return value

factorial(3)
factorial(5)

#10
import random

highest = 10

while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break


#11
my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

num_lists = len(my_list)
print(num_lists)

counter1 = 0
counter2 = 0
list1 = []

while counter1 < num_lists:
    
    list1 = my_list[counter1]
    #print(f'Length of list1: {len(list1)}')
    #print(f'List1 : {list1}')
    #print(f'counter1 : {counter1}')
    
    while counter2 < len(list1):
        num = list1[counter2]
        if num % 2 == 0:
            print(num)
        counter2 += 1    
    
    list1 = []
    counter2 = 0
    counter1 += 1
    
