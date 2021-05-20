user_in = input('Type what you want to reverse\n')
splitted = user_in.split()

for j in reversed(splitted): #reverse list
    print(j)


for i in reversed(user_in):#reverse word
    print(i)
