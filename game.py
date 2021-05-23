import random
import os
import time
def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

# Set of instructions for Rock-Paper-Scissors-Lizard-Spock
def rpsls_instructions():
    print()
    print("Instructions for Rock-Paper-Scissors-Lizard-Spock : ")
    print()
    print("Scissors cuts Paper")
    print("Paper covers Rock")
    print("Rock crushes Lizard")
    print("Lizard poisons Spock")
    print("Spock smashes Scissors")
    print("Scissors decapitates Lizard")
    print("Lizard eats Paper")
    print("Paper disproves Spock")
    print("Spock vaporizes Rock")
    print("Rock crushes Scissors")
    print()


def rpsls():
    global rpsls_table
    global game_map
    global name

    # Game Loop for each game of Rock-Paper-Scissors-Lizard-Spock
    while True:
        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Enter \"help\" for instructions")
        print("Enter \"Rock\",\"Paper\",\"Scissors\",\"Lizard\",\"Spock\" to play")
        print("Enter \"exit\" to quit")
        print("--------------------------------------")

        print()

        # Player Input
        inp = input("Enter your move : ")

        if inp.lower() == "help":
            cls()
            rpsls_instructions()
            continue
        elif inp.lower() == "exit":
            cls()
            break
        elif inp.lower() == "rock":
            player_move = 0
        elif inp.lower() == "paper":
            player_move = 1
        elif inp.lower() == "scissors":
            player_move = 2
        elif inp.lower() == "lizard":
            player_move = 3
        elif inp.lower() == "spock":
            player_move = 4
        else:

            print("Wrong Input!!")
            rpsls_instructions()
            continue

        print("Computer making a move....")

        comp_move = random.randint(0, 4)
        print()
        time.sleep(2)

        print("Computer chooses ", game_map[comp_move].upper())

        winner = rpsls_table[player_move][comp_move]
        print()
        if winner == player_move:
            print(name, "WINS!!!")
        elif winner == comp_move:
            print("COMPUTER WINS!!!")
        else:
            print("TIE GAME")
        print()
        time.sleep(2)
        cls()


# The main function
if __name__ == '__main__':

    # The mapping between moves and numbers
    game_map = {0: "rock", 1: "paper", 2: "scissors", 3: "lizard", 4: "Spock"}

    # Win-lose matrix for new version of the game
    rpsls_table = [[-1, 1, 0, 0, 4], [1, -1, 2, 3, 1], [0, 2, -1, 2, 4], [0, 3, 2, -1, 3], [4, 1, 4, 3, -1]]

    name = input("Enter your name: ")

    # The GAME LOOP
    while True:

        # The Game Menu
        print()
        print(name, "let's play!!!")
        print("Enter 1 to play Rock-Paper-Scissors-Lizard-Spock")
        print("Enter 2 to quit")
        print()

        # Try block to handle the player choice
        try:
            choice = int(input("Enter your choice = "))
        except ValueError:
            cls()
            print("Wrong Choice")
            continue

        # Play the new version of the game
        if choice == 1:
            rpsls()

        # Quit the GAME LOOP
        elif choice == 2:
            break

        # Other wrong input
        else:
            cls()
            print("Wrong choice. Read instructions carefully.")
