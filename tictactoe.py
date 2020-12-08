board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]


def display():
    print(9 * "-")
    for i in range(0, len(board), 3):
        print(f"| {' '.join(board[i:i + 3])} |")
    print(9 * "-")


display()

player_1_turn = True

player_1_win = False
player_2_win = False
draw = False
empty = 9

while True:
    x, y = input("Enter the coordinates: ").split()
    if x.isdecimal() and y.isdecimal():
        index = abs((int(x) - 1) + (9 - (3 * int(y))))
        if index > 8:
            print("Coordinates should be from 1 to 3!")
        elif board[index] != " ":
            print("This cell is occupied! Choose another one!")
        elif index <= 8:
            if player_1_turn:
                board[index] = "X"
                player_1_turn = False
            else:
                board[index] = "O"
                player_1_turn = True
            display()
    else:
        print("You should enter numbers!")

    for i in range(len(board)):
        if i < 3 and board[i] != " ":
            if board[i] == board[i + 3] == board[i + 6]:
                if board[i] == "X":
                    player_1_win = True
                else:
                    player_2_win = True
    if board[0] == board[4] == board[8] and board[0] != " ":
        if board[0] == "X":
            player_1_win = True
        else:
            player_2_win = True
    if board[2] == board[4] == board[6] and board[2] != " ":
        if board[2] == "X":
            player_1_win = True
        else:
            player_2_win = True

    empty = sum([c == " " for c in board])

    if player_1_win:
        print("X wins")
        break
    elif player_2_win:
        print("O wins")
        break
    elif empty == 0:
        print("Draw")
        break
