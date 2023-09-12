field = list(range(1, 10))

def board(field):
    for i in range(3):
        print("", field[0 + i * 3], "", field[1 + i * 3], "", field[2 + i * 3], "")

def take_input(player_token):
    correct = False
    while not correct:
        player_move = input("Значение " + player_token + "? ")
        try:
            player_move = int(player_move)
        except ValueError:
            print("Некорректный ввод")
            continue
        if 1 <= player_move <= 9:
            if str(field[player_move - 1]) not in "XO":
                field[player_move - 1] = player_token
                correct = True
            else:
                print("Эта клетка занята!")
        else:
            print("Введите число от 1 до 9.")
def win_lines(field):
    win_numbers = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for cycle in win_numbers:
        if field[cycle[0]] == field[cycle[1]] == field[cycle[2]]:
            return field[cycle[0]]
    return False
def main(field):
    counter = 0
    win = False
    while not win:
        board(field)
        if counter % 2 == 0:
            take_input("X")
        else:
            take_input("O")
        counter += 1
        tmp = win_lines(field)
        if tmp:
            print(tmp, "выиграл!")
            win = True
            break
        if counter == 9:
            print("Ничья!")
            break
    board(field)
main(field)
input("Нажмите Enter для выхода!")