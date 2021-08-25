import copy
import os


def start_battleship():
    global boardsize, numbers, alphabet
    player1_name = input("What is the name of Player One ? ")
    player2_name = input("What is the name of Player Two ? ")
    boardsize = int(input("Size of board : "))
    turn_number = int(input("Number of Turn : "))
    player1_board = []
    for x in range(boardsize):
        player1_board.append(["--"] * boardsize)

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphabet = alphabet[:boardsize]
    numbers = []
    count = 1
    score1 = 0
    score2 = 0
    player2_board = copy.deepcopy(player1_board)
    choose1_board = copy.deepcopy(player1_board)
    choose2_board = copy.deepcopy(player1_board)
    for n in range(boardsize):
        numbers.append(str(count))
        count += 1

    print("****** %s's Turn to put his ships on board ******" % player1_name)
    print_board(player1_board)
    choose_ships_location(player1_board)
    print("****** %s's Turn to put his ships on board ******" % player2_name)
    print_board(player2_board)
    choose_ships_location(player2_board)
    t = 1
    while t < turn_number * 2 + 1:
        if t % 2 == 1:
            print("*****  %s's turn to shoot  *****" % player1_name)
            print_board(choose1_board)
            shoot_location(choose1_board, player2_board, t)
            print("*****  Score Board is  *****: ")
            print(player1_name, ":", score1)
            print(player2_name, ":", score2)
        else:
            print("*****  %s's turn to shoot  *****" % player2_name)
            print_board(choose2_board)
            shoot_location(choose2_board, player1_board, t)
            print("**** Score Board is ****: ")
            print(player1_name, ":", score1)
            print(player2_name, ":", score2)
        t += 1

    if score1 > score2:
        print("*** Congratulations", player1_name, "You Win ***")
    if score2 > score1:
        print("*** Congratulations", player1_name, "You Win ***")
    if score1 == score2:
        print("****  Game was Draw  ****")
    print("")


def print_board(board):
    count = 1
    if boardsize < 10:
        print(" ", "   ".join(numbers))
        count += 1
    else:
        print(" ", "   ".join(numbers[:10]), " ".join(numbers[10:]))
    count = 0
    for row in board:
        print(alphabet[count], "  ".join(row))
        count += 1


def choose_ships_location(board):
    c = 0
    while c < 4:
        os.system('cls')
        print_board(board)
        print("You have ", 4-c, "submarine(1)")
        pos = input("Location of ship : ")
        pos = pos.upper()
        if len(pos) > 3 or len(pos) < 2 or int(pos[1:]) > boardsize or pos[0] not in alphabet:
             print("Your Entry is wrong")
             continue
        if fill_board(board, pos) == 0:
             continue
        else:
             fill_board(board, pos)
             c += 1
    while c > 1:
        num = 2
        os.system('cls')
        print_board(board)
        print("You have ", c - 1, "destroyer(2)")
        pos = input("Location of ship : ")
        pos = pos.upper()
        if len(pos) > 3 or len(pos) < 2 or int(pos[1:]) > boardsize or pos[0] not in alphabet:
             print("Your Entry is wrong")
             continue
        else:
            dir = input("Direction of ship(Down:d   Right:r) : ")
            dir = dir.upper()
            if dir not in ["D", "R"]:
                print("Your Entry is wrong")
                continue
            if is_valid(board, pos, dir, num) == 0:
                print("Your Entry is wrong")
                continue
            else:
                fill_direction(board, pos, dir, num)
                c -= 1
    while c < 3:
        num = 3
        os.system('cls')
        print_board(board)
        print("You have ", 4-c, "cruiser(3)")
        pos = input("Location of ship : ")
        pos = pos.upper()
        if len(pos) > 3 or len(pos) < 2 or int(pos[1:]) > boardsize or pos[0] not in alphabet:
             print("Your Entry is wrong")
             continue
        else:
            dir = input("Direction of ship(Down:d   Right:r) : ")
            dir = dir.upper()
            if dir not in ["D", "R"]:
                print("Your Entry is wrong")
                continue
            if is_valid(board, pos, dir, num) == 0:
                print("Your Entry is wrong")
                continue
            else:
                fill_direction(board, pos, dir, num)
                c += 1
    while c > 2:
        num = 4
        os.system('cls')
        print_board(board)
        print("You have ", c - 1, "battleship(4)")
        pos = input("Location of ship : ")
        pos = pos.upper()
        if len(pos) > 3 or len(pos) < 2 or int(pos[1:]) > boardsize or pos[0] not in alphabet:
             print("Your Entry is wrong")
             continue
        else:
            dir = input("Direction of ship(Down:d   Right:r) : ")
            dir = dir.upper()
            if dir not in ["D", "R"]:
                print("Your Entry is wrong")
                continue
            if is_valid(board, pos, dir, num) == 0:
                print("Your Entry is wrong")
                continue
            else:
                fill_direction(board, pos, dir, num)
                c -= 1
    else:
        print("\n" * 30)


def fill_board(board, pos):
    a = ord(pos[0]) - 65
    b = int(pos[1:]) - 1
    if board[a][b] == "--":
        board[a][b] = "##"
    else:
        return False


def fill_direction(board, pos, dir, num):
     a = ord(pos[0]) - 65
     b = int(pos[1:]) - 1
     while num > 0:
        board[a][b] = "##"
        if dir == "D":
             a += 1
        if dir == "R":
             b += 1
        num -= 1


def is_valid(board, pos, dir, num):
    a = ord(pos[0]) - 65
    b = int(pos[1:]) - 1
    while num > 0:
        if str(a+1) not in numbers or str(b+1) not in numbers or board[a][b] == "##":
            return False
        else:
            if dir == "D":
                a += 1
            if dir == "R":
                b += 1
            num -= 1
    else:
        return True


def shoot(board, pos, goal_board, t):
    global score1
    global score2
    a = ord(pos[0]) - 65
    b = int(pos[1:]) - 1
    if goal_board[a][b] == "##":
        board[a][b] = "HH"
        if t % 2 == 1:
            score1 += 1
        else:
            score2 += 1
        print("**** Yesss Hit ****")
    if goal_board[a][b] == "--":
        board[a][b] = "@@"
        print("**** No ****")


def shoot_location(board, board_o, t):
    count = 0
    while count < 1:
        pos = input("Location for shoot : ")
        pos = pos.upper()
        if len(pos) > 3 or len(pos) < 2 or int(pos[1:]) > boardsize or pos[0] not in alphabet:
            print("Your Entry is wrong")
            continue
        if fill_board(board, pos) == 0:
            continue
        else:
             os.system('cls')
             shoot(board, pos, board_o, t)
             print_board(board)
        count += 1