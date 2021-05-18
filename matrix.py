matrix_B = [[4, 5, 6],
            [9, 8, 7],
            [3, 2, 1]]

matrix_A = [[3, 2, 1],
            [4, 5, 6],
            [7, 8, 9]]


def add_matrixes(matA, matB):
    for i in range(3): #columns
        for k in range(3): #rows
            matrix_result = matA[i][k] + matB[i][k]
            print(f'{matrix_result}')


def sub_matrixes(matA, matB):
    for i in range(3): #columns
        for k in range(3): #rows
            matrix_result = matA[i][k] - matB[i][k]
            print(f'{matrix_result}')

def mul_matrixes(matA, matB):
    for i in range(3): #columns
        for k in range(3): #rows
            matrix_result = matA[i][k] * matB[i][k]
            print(f'{matrix_result}')


while True:
    in_user = input('What do you want to do with matrixes? subtraction=s, addition=a, multilpy=m \n')
    if in_user == str('a'):
        add_matrixes(matrix_A, matrix_B)
    elif in_user == str('s'):
        sub_matrixes(matrix_A, matrix_B)
    elif in_user == str('m'):
        mul_matrixes(matrix_A, matrix_B)
    else:
        print('Type only \'s\', \'m\', \'a\'')
