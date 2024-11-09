import sys


def RockPaperScissors():
    import RockPaperScissors

def TickTokTa():
    pass

def exit():
    sys.exit()

def Games():
    games = {
        '1': ('Tik Tok Ta',TickTokTa),
        '2': ('Rock Paper Sciccors',RockPaperScissors),
        '3': ('Exit',exit)
    }
    print("System22 games \n")
    for key, (name,_) in games.items():
        print(f'{key}. {name}')
    choice = input("Enter your choice: ")

    if choice in games:
        game_name, game = games[choice]
        print(f'######### Now Strting {game_name}')
        game()
    else:
        print("Invalid choice! Please try again.")

Games()
