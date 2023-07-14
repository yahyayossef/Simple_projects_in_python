c1 = "1"
c2 = "2"
c3 = "3"
c4 = "4"
c5 = "5"
c6 = "6"
c7 = "7"
c8 = "8"
c9 = "9"
turn_num = 0
character = ""
chooses = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]


def print_game():
    print("|-----------------------------------------------|")
    print(f"|\t {c1} \t|\t {c2} \t|\t {c3} \t|")
    print("|-----------------------------------------------|")
    print(f"|\t {c4} \t|\t {c5} \t|\t {c6} \t|")
    print("|-----------------------------------------------|")
    print(f"|\t {c7} \t|\t {c8} \t|\t {c9} \t|")
    print("|-----------------------------------------------|")


def replace():
    global c1, c2, c3, c4, c5, c6, c7, c8, c9
    if turn == "1":
        c1 = character
    elif turn == "2":
        c2 = character
    elif turn == "3":
        c3 = character
    elif turn == "4":
        c4 = character
    elif turn == "5":
        c5 = character
    elif turn == "6":
        c6 = character
    elif turn == "7":
        c7 = character
    elif turn == "8":
        c8 = character
    elif turn == "9":
        c9 = character


def donot_take():
    global turn
    while turn not in chooses:
        print("This position is busy or not valid")
        turn = input(f"Turn of {character}:- ")


def win():
    if (c1 == c2 == c3) or (c4 == c5 == c6) or (c7 == c8 == c9) or (c1 == c4 == c7) or (c2 == c5 == c8) or (c3 == c6 == c9) or (c1 == c5 == c9) or (c3 == c5 == c7):
        print_game()
        print(f"{character} wins")
        return True


print("Welcome to X-O game")
print("Choose number to replace it by character")
while True:
    print_game()
    turn_num += 1
    if turn_num % 2 == 1:
        character = "O"
    elif turn_num % 2 == 0:
        character = "X"

    turn = input(f"Turn of {character}:- ")
    donot_take()
    chooses.remove(turn)
    replace()
    if chooses == []:
        print("Draw")
        break
    if win() == True:
        break
