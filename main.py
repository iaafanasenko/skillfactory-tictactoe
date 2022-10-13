player_info = ({"info": "первый", "text": "X"}, {"info": "второй", "text": "0"})

field = [[" " for row in range(3)] for column in range(3)]

current_player = 0

turn = 1


def show_field(field):
    print(f"   | 0 | 1 | 2 ")
    print("---|---|---|---")
    for row, column in enumerate(field):
        data = f" {row} | {' | '.join(column)}"
        print(data)
        print("---|---|---|---")


def get_answer(player):
    print("")
    answer = input(f"\033[32mХодит {player['info']} игрок ({player['text']}): \033[0m").split()
    print("")

    return answer


def check_answer(field, answer):
    if len(answer) != 2:
        print(f"\033[31mВведите две координаты (номер строки и номер столбца).\033[0m")
        return False

    row, column = answer

    if not(row.isdigit()) or not(column.isdigit()):
        print(f"\033[31mВведите два числа: x y\033[0m")
        print("x - номер строки")
        print("y - номер столбца")
        return False

    row, column = int(row), int(column)

    if not(0 <= row <= 2 and 0 <= column <= 2):
        print(f"\033[31mУказанные координаты выходят за пределы диапазона.\033[0m")
        return False

    if field[row][column] != " ":
        print(f"\033[31mКлетка занята.\033[0m")
        return False

    return row, column


def check_win(player, field):
    variants = (((0, 0), (0, 1), (0, 2)),  # Горизонталь 1
                ((1, 0), (1, 1), (1, 2)),  # Горизонталь 2
                ((2, 0), (2, 1), (2, 2)),  # Горизонталь 3
                ((0, 0), (1, 0), (2, 0)),  # Вертикаль 1
                ((0, 1), (1, 1), (2, 1)),  # Вертикаль 2
                ((0, 2), (1, 2), (2, 2)),  # Вертикаль 3
                ((0, 0), (1, 1), (2, 2)),  # Диагональ 1
                ((2, 0), (1, 1), (0, 2))   # Диагональ 2
                )

    for combination in variants:
        coord1 = combination[0]
        coord2 = combination[1]
        coord3 = combination[2]

        if field[coord1[0]][coord1[1]] == field[coord2[0]][coord2[1]] == field[coord3[0]][coord3[1]] == player:
            return True
    return False


def change_player(current_player):
    if current_player == 0:
        next_player = 1
    else:
        next_player = 0

    return next_player


print("\033[34mИгра 'Крестики-нолики'\033[0m")
print("")
print("Формат ввода: x y")
print("x - номер строки")
print("y - номер столбца")
print("")

show_field(field)
user_answer = get_answer(player_info[current_player])

while True:
    if check_answer(field, user_answer):
        row, column = check_answer(field, user_answer)

        field[row][column] = player_info[current_player]["text"]

        if turn == 9:
            print("")
            print(f"\033[33mПобедила дружба!\033[0m")
            print("")

            show_field(field)
            break
        elif check_win(player_info[current_player]["text"], field):
            print("")
            print(f"\033[33mВыиграл {player_info[current_player]['info']} игрок ({player_info[current_player]['text']}). Поздравляем!\033[0m")
            print("")

            show_field(field)
            break
        else:
            current_player = change_player(current_player)

            turn += 1

            show_field(field)

            user_answer = get_answer(player_info[current_player])
    else:
        user_answer = get_answer(player_info[current_player])
        continue
