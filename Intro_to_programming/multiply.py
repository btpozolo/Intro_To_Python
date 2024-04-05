
num_1 = input('Enter the first number: ')
num_2 = input('Enter the second number: ')
print(f' {float(num_1)} * {float(num_2)} = {float(num_1) * float(num_2)}')
    
def remainders_3(numbers):
    return [number % 3 for number in numbers]


numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

any(remainders_3(numbers_1)) != 0
any(remainders_3(numbers_2)) != 0
any(remainders_3(numbers_3)) != 0
any(remainders_3(numbers_4)) != 0

print(any(remainders_3(numbers_1)))     # True
print(any(remainders_3(numbers_2)))     # True
print(any(remainders_3(numbers_3)))     # False
print(any(remainders_3(numbers_4)))     # False


def remainders_5(numbers):
    return [number % 5 for number in numbers]


numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

print(remainders_5(numbers_1))
any(remainders_5(numbers_1))
all(remainders_5(numbers_2))

print(all(remainders_5(numbers_1)))
print(all(remainders_5(numbers_2)))
print(all(remainders_5(numbers_3)))
print(all(remainders_5(numbers_4)))


print(any(remainders_5(numbers_1)) == 0)
print(any(remainders_5(numbers_2)) == 0)
print(any(remainders_5(numbers_3) == 0))
print(any(remainders_5(numbers_4) == 0))