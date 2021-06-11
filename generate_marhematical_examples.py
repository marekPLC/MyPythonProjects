import random
import time

counter = 0
number_list = []

def sign():
    list_sign = ['-', '+']
    return random.choice(list_sign)


for i in range(5):
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    if sign() == '+':
        print(f'{x} + {y}')
        result = x + y
        usr_input = input('Type result \n')
        if int(usr_input) == result:
            counter += 1
        else:
            counter -= 1
    else:
        print(f'{x} - {y}')
        result = x - y
        usr_input = input('Type result \n')
        if int(usr_input) == result:
            counter += 1
        else:
            counter -= 1

print(f'Now you have {counter} points')

for i in range(10):
    x = (random.randint(1, 100))
    print(x)
    number_list = number_list.append(x)
    time.sleep(1)
    if i == 10:
        print(number_list)
        number_input = input('How many numbers did u remember? Type them')

