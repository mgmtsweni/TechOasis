import getpass
import random
import sys


print("Rock-Paper-Scissors!! \n")
print("Who do you want to play  against")
print("1. Human vs Human\n2. Human vs AI\n3. Exit!!")
choice = input("Enter your choice: ")

if choice == "1":
    print("Human vs Human. Let's go!!")
    while True:
        print("Player 1 starts")
        player_1 = getpass.getpass("Rock, Paper or Scissors: ").capitalize()
        print("Player 2 starts")
        player_2 = getpass.getpass("Rock, Paper or Scissors: ").capitalize()
        print("Player 1: ", player_1 + "\nPlayer 2: ", player_2)
        if player_1 == player_2:
            print("It's a tie.")
        elif player_1 == "Rock":
            if player_2 == "Paper":
                print("Player 2 wins\n")
            elif player_2 == "Scissors":
                print("player 1 wins\n")
            else:
                print("Invalide entery found\n")
        elif player_1 == "Paper":
            if player_2 == "Rock":
                print("player 1 wins\n")
            elif player_2 == "Scissors":
                print("Player 2 wins\n")
            else:
                print("Invalide entery found\n")
        elif player_1 == "Scissors":
            if player_2 == "Rock":
                print("Player 2 wins\n")
            elif player_2 == "Paper":
                print("player 1 wins\n")
            else:
                print("Invalide entery found\n")
        else:
            break
elif choice == "2":
    print("\nHuman vs Ai. Let's go!!")
    while True:
        choices = {1: "Rock", 2: "Scissors", 3: "Paper"}
        comp = choices[random.randint(1, 3)]
        player = input("Rock, Paper or Scissors\nChoose: ").capitalize()
        print("AI's choice:", comp + "\nPlayer's choice:", player)

        if player == comp:
            print("It's a tie.\n")
        elif (player == "Rock" and comp == "Scissors") or \
            (player == "Paper" and comp == "Rock") or \
            (player == "Scissors" and comp == "Paper"):
            print("Player wins.\n")
        elif (player == "Rock" and comp == "Paper") or \
            (player == "Paper" and comp == "Scissors") or \
            (player == "Scissors" and comp == "Rock"):
            print("AI wins.\n")
        else:
            print("Invalid entry found\n")
            break
    
elif choice == "3":
    sys.exit() 
else:
    print("Invalid choice! Please try again.")
