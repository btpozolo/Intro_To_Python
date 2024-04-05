value = int(input('Enter a number: '))

if value == 3:
    print('value is 3')
else:
    if value == 4:
        print('value is 4')
    else:
        print('value is NOT 3 or 4')

def even_or_odd(number):
    if number % 2 == 0:
        print('even')
    else:
        print('odd')

even_or_odd(5)
even_or_odd(6)

if foo():
    'bar'
else:
    qux()

def capitalize(my_string):
    if len(my_string) > 10:
        return str(my_string).upper()
    else:
        return str(my_string)

capitalize('hello world')
capitalize('goodbye')

def int_range(my_int):
    if my_int < 0:
        print('this value is less than 0')
    elif my_int < 51:
        print('this value is between 0 and 50')
    elif my_int < 101:
        print('this value is between 51 and 100')
    else:
        print('this value is greater than 100')