import random

list_range = [1, 100]  # numbers range
tries = 3
guessed = False

while True:
    try:
        user_input = int()
        user_input = int(input(f'Type your guess between {list_range[0]} and {list_range[1]}. You have {tries} tries \n'))
    except ValueError:
        print('Type int value')


    def random_number(range1, range2, guess_user):
        global guessed
        global tries
        x = random.randint(range1, range2)
        if guess_user > range2 and guess_user < range1:
            print(f'Type int value between {range1} and {range2}.')
        else:
            if user_input == x:
                print('You guessed the number! Good job.')
                guessed = True
                exit()
            else:
                print(f'Bad guess, try it again. The number was {x}')
                guessed = False
                tries -= 1
                if tries == 0:
                    print(f'This was your last try:(.')
                    exit()


    print(random_number(list_range[0], list_range[1], user_input))
