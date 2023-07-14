import random

# Welcoming message
print("--------------------------")
print("Rock, Paper, Scissors Game")
print("--------------------------")

# Storing rules of game in variable
rules = """
Rulers:-
    1- You can choose rock or paper or scissors only
    3- To exit from the game enter 'q' letter
"""

# List of choices in game
items = ["Rock", "Paper", "Scissors"]
# List of win cases
wins1 = ["Rock", "Scissors"]
wins2 = ["Scissors", "Paper"]
wins3 = ["Paper", "Rock"]

# Printing the rules
print(rules)

# Storing name of player in the variable p1_name
p1_name = input("Enter your name:- ")


# Function who stores choices of players in two variable
def inputs():
    global p1, p2
    p1 = input(f"{p1_name} : Enter your choice:- ").strip().capitalize()
    p2 = items[random.randint(0, 2)]


# Function who check that choice of player one and two equal each other
# , if that true she will return true else don`t return any thing
def check_inputs():
    global p2
    if p1 == p2:
        while p1 == p2:
            p2 = items[random.randint(0, 2)]
        return True


# Function who print the expression of win case
def check_cases():
    if p1 in wins1 and p2 in wins1:
        return "Rock broke the Scissors"

    elif p1 in wins2 and p2 in wins2:
        return "Scissors cut the paper"

    elif p1 in wins3 and p2 in wins3:
        return "Paper covered the Rock"


# Function who print name of winner
def print_winner():
    sentences = check_cases().split()
    if p1 == sentences[0]:
        print(f"{p1_name} is the winner")

    elif p2 == sentences[0]:
        print(f"Computer is the winner")


# Game loop
while True:
    inputs()
    while p1 not in items and p1 != "Q":
        print("Wrong ,you should enter rock or paper or scissors only")
        inputs()
    if p1 == "Q":
        break
    if check_inputs() == True:
        pass

    print(f"Computer choice :- {p2}")
    print(check_cases())
    print_winner()
    print("-" * 60)
