user_in = input('Type what you want to reverse\n')
splitted = user_in.split()
print(splitted)

for i in reversed(splitted):
    print(i)