import Battleship
import Quoridor

a = 0
print("")
while a != 3:
    print("Choose \n 1.Battleship \n 2.Quoridor \n 3.Exit")
    a = int(input())
    if a == 1:
        Battleship.start_battleship()
    if a == 2:
        Quoridor.start_quoridor()
