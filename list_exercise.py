#get numbers around specific number in list


import random

list = [10, 5, 3, 4, 19, 1, 3, 5]


def add(arg1, arg2):
    result = arg1 + arg2
    print(result)


def sub(arg1, arg2):
    result = arg1 - arg2
    print(result)


def get_random(arg):
    print(f'{arg} list input')
    random_in_list = random.choice(arg)
    print(f'{random_in_list} is number in list')
    if random_in_list in arg:
        x = list.index(random_in_list)
        print(f'{x} is index of number {random_in_list}')
        y = list[x-1]
        z = list[x+1]
        user_input = input(f'Numbers around required number {y}, {z}. Type \'+\' for add numbers, \'-\' for sub \n')
        if user_input == '+':
            add(y, z)
        else:
            sub(y, z)


get_random(list)

