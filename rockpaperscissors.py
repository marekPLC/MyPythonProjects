import random


list = ['rock', 'paper', 'scissors']
user_input = str(input('Type you guess \n'))
guessed = False


def random_def(var):
    x = random.choice(list)
    print(x)
    if x == var:
        guessed = True
        return print(f'Good choice, good game! It was {x}'), guessed
    else:
        guessed = False
        return print(f'Try again :(, the word was {x}'), guessed


print(random_def(user_input))
