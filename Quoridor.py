def start_quoridor():
    global numbers, alphabet, player1_name, player2_name, board
    player1_name = input("What is the name of Player One(XX) ? ")
    player2_name = input("What is the name of Player Two(OO) ? ")
    boardsize = 9
    board = []
    for x in range(boardsize * 2 - 1):
        board.append(["  "] * (2 * boardsize - 1))

    alphabet = "ABCDEFGH"
    numbers = []
    count = 1
    a, b = 0, 8
    x, y = 16, 8
    t = 1
    d =[[], [], [], [], [], [], [], [], []]
    player1_sign = " X"
    player2_sign = " O"
    player1_border = 10
    player2_border = 10
    board[a][b] = " X"
    board[x][y] = " O"
    for n in range(boardsize):
        numbers.append(str(count))
        count += 1

    while " O" not in board[0] or " X" not in board[16]:
        print_board(board)
        if t % 2 == 1:
            if get_input(player1_name, player1_sign, player1_border, a, b) == 0:
                print("Your Entry is wrong")
                continue
        else:
            if get_input(player2_name, player2_sign, player2_border, x, y) == 0:
                print("Your Entry is wrong")
                continue
        t += 1
    else:
        if " O" in board[0]:
            print(player2_name, " is win")
        if " X" in board[16]:
            print(player1_name, " is win")

def print_board(board):
    count = 0
    c = 0
    print("   1   A   2   B   3   C   4   D   5   E   6   F   7   G   8   H   9")
    while count < 8:
        print(numbers[count], "  ".join(board[c]), "\n")
        print(alphabet[count], "  ".join(board[c+1]), "\n")
        count += 1
        c += 2
    else:
        print(numbers[count], "  ".join(board[c]), "\n")


def get_input(player_name, player_sign, player_border, f, g):
    print("%s is X  and  " % player1_name, end="")
    print("%s is O" % player2_name)
    print("%s , You have " % player_name, end="")
    print("%d border" % player_border)
    pos = input("%s Please Enter the location of Move or Border(numeric for Move and alphabetic for Border) : " %player_name)
    pos = pos.upper()
    if not 4> len(pos) > 1:
        return False
    else:
        if len(pos) == 3:
            if pos[0] not in alphabet or pos[1] not in alphabet or pos[2] not in ["H","V"]:
                return False
            else:
                border(board, pos, player_sign)
        else:
            if pos[0] not in numbers or pos[1] not in numbers:
                return False
            else:
                if move(board, pos, f, g, player_sign) == 0:
                    return False


def move(board, pos, f, g, player_sign):
    global a, b, x, y
    i = 2 * int(pos[0]) - 2
    j = 2 * int(pos[1]) - 2
    if i not in range(17) or j not in range(17):
        return False
    elif f == i:
        if g == j - 2:
            if board[i][j - 1] != "||":
                board[i][j] = player_sign
                board[f][g] = "  "
                if player_sign == " X":
                    b = j
                else:
                    y = j
            else:
                return False
        elif g == j + 2:
            if board[i][j + 1] != "||":
                board[i][j] = player_sign
                board[f][g] = "  "
                if player_sign == " X":
                    b = j
                else:
                    y = j
            else:
                return False
        else:
            return False
    elif g == j:
        if f == i - 2:
            if board[i - 1][j] != "--":
                board[i][j] = player_sign
                board[f][g] = "  "
                if player_sign == " X":
                    a = i
                else:
                    x = i
            else:
                return False
    else:
        return False


def border(board, pos, player_sign):
    global player1_border, player2_border
    i = 2 * (ord
             (pos[0]) - 65) + 1
    j = 2 * (ord(pos[1]) - 65) + 1
    if i not in range(17) or j not in range(17):
        return False
    else:
        if pos[2] == "H":
            board[i][j - 1] = "--"
            board[i][j] = "--"
            board[i][j + 1] = "--"
            if player_sign == " X":
                player1_border -= 1
            if player_sign == " O":
                player2_border -= 1
        if pos[2] == "V":
            board[i - 1][j] = "||"
            board[i][j] = "||"
            board[i + 1][j] = "||"
            if player_sign == " X":
                player1_border -= 1
            if player_sign == " O":
                player2_border -= 1
        else:
            return False
