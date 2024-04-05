def say(text):
    print('==> ' + text)

say('hello')
say('hi')
say('how do you do')
say('Quite all right')

def add(a, b):
    return a + b

two_and_three = add(2, 3)
print(two_and_three)  # 5

def say(text='hello'):
    print(text + '!')

say('Howdy') # Howdy!
say()        # hello!