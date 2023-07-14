from random import randint
from pyfiglet import figlet_format
from termcolor import colored
from string import ascii_uppercase

print("=========================================")
print("======== Hello in hang man game =========")
print("=========================================")

easy = ["CODE", "LIFE", "WORD", "GAME", "GOOD", "LOOP"]
middle = ["MASTER", "SUBMIT", "STUDIO", "PYTHON", "HORROR", "SYSTEM"]
hard = ["PROJECT", "COMPUTER", "LANGUAGE", "OPERATOR", "GRAPHICS", "DOWNLOAD"]

hangman = [
    """
     -------
    |       |
    |        
    |        
    |
    |
|---------|
""",
    """
     -------
    |       |
    |       0 
    |        
    |
    |
|---------|
""",
    """
     -------
    |       |
    |       0 
    |       |
    |
    |
|---------|
""",
    """
     -------
    |       |
    |       0 
    |       |\\
    |       
    |
|---------|
""",
    """
     -------
    |       |
    |       0 
    |      /|\\
    |       |
    |       
    |
|---------|
""",
    """
     -------
    |       |
    |       0 
    |      /|\\
    |       |
    |        \\
    |
|---------|
""",
    """
     -------
    |       |
    |       0 
    |      /|\\
    |       |
    |      / \\
    |
|---------|
""",
]

print(hangman[0])


def choice_mode():
    global game_list, mode
    mode = input("Choose mode of the game [easy, middle, hard]:- ").lower().strip()
    if mode == "easy":
        game_list = easy

    elif mode == "middle":
        game_list = middle

    elif mode == "hard":
        game_list = hard

    else:
        print("Choose easy, middle, hard only\n")
        choice_mode()


choice_mode()
print(f"Your choice {mode} mode\n")


word = list(game_list[randint(0, len(game_list) - 1)])
underscore_word = ("_ " * len(word)).split()
tries = 6


def variables():
    global word, underscore_word, tries
    word = list(game_list[randint(0, len(game_list) - 1)])
    underscore_word = ("_ " * len(word)).split()
    tries = 6


def num_chars():
    count = 0
    for i in word:
        if i != "":
            count += 1
    return count


def if_continue():
    global response
    choice = input("Do you want to play again [y, n] :- ").lower()
    if choice == "y" or response == True:
        response = True
        return True
    elif choice == "n":
        return False
    else:
        print("!!!!! Enter 'y' or 'n' letter only !!!!!\n")
        response = if_continue()


while True:
    response = None
    print(f"\nword length {len(word)} - {num_chars()} letters left")
    guess = input("Guess letter of the word :- ").upper().strip()

    if guess not in ascii_uppercase or guess == "":
        print("\n!!!!! Enter letter only !!!!!")
        continue

    if guess in underscore_word:
        print("\nYou already entered this letter")
        continue

    if guess in word:
        print("\nExcellent - that `s right letter")
        for l in word:
            if l == guess:
                get_index = word.index(l)
                word[get_index] = ""
                underscore_word[get_index] = guess
        print("".join(underscore_word))

    else:
        print(hangman[6 - tries])
        tries -= 1
        if tries != 0:
            print("\nWrong - Weird")
            print(f"\nYou have {tries} tries")
            print("".join(underscore_word))

        elif tries == 0:
            print("\nHard luck next time")
            print(colored(figlet_format("You lose"), color="red"))

    if num_chars() == 0:
        print("Congratulation\n")
        print(colored(figlet_format("You won"), "blue"))

    if tries == 0 or num_chars() == 0:
        if_continue()
        if response == True:
            choice_mode()
            print(f"\nYour choice {mode} mode")
            variables()
        else:
            break
