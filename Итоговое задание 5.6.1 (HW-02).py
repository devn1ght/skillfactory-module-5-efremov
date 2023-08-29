print('Игра Крестики-нолики')


def initialize_matrix():
    return [['-', '-', '-'],
            ['-', '-', '-'],
            ['-', '-', '-']]


def matrix_():
    for i in matrix:
        print(*i)


def play(play_choice):
    while True:
        string = int(input('Введите строку: '))
        if string > 2 or string < 0:
            print('Неверные координаты')
            continue

        column = int(input('Введите столбец: '))
        if column > 2 or column < 0:
            print('Неверные координаты')
            continue

        if matrix[string][column] == '-':
            matrix[string][column] = play_choice
            matrix_()
            print('__')

            if check_win(play_choice):
                print(play_choice, "Победа!")
                return True

            break

        else:
            print('Эта ячейка уже занята!')

    return False


def check_win(player):
    for i in range(3):
        if all(matrix[i][j] == player for j in range(3)) or all(matrix[j][i] == player for j in range(3)):
            return True

    if all(matrix[i][i] == player for i in range(3)) or all(matrix[i][2 - i] == player for i in range(3)):
        return True

    return False


while True:
    matrix = initialize_matrix()
    matrix_()

    count = 0
    while count < 9:
        if count % 2 == 0:
            print('Ходит крестик!')
            if play('X'):
                break
        else:
            print('Ходит нолик!')
            if play('0'):
                break

        count += 1
    else:
        print('Ничья!')

    restart = input("Хотите сыграть еще раз? (да/нет): ")
    if restart.lower() != "да":
        break
