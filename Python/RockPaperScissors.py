from tkinter import * # type: ignore
import random

root = Tk()
root.title('CodSoft')
root.geometry('950x600+10+10')
root.resizable(0, 0) # type: ignore

def playAgain():
    root.destroy()
    import RockPaperScissors

def gameLogic(player):
    pitchFrame = Listbox(groundFrame, width=58, height=19)
    pitchFrame.place(x=165, y=0)
    pitchtext = Text(groundFrame, width=57, height=5)
    pitchtext.place(x=167, y=100)
    btnScissors = Button(pitchFrame, text='Play Again?', bd=0, activeforeground='black',
                        bg='white', fg="black", font=('Arial', 15, 'bold'), command=playAgain)
    btnScissors.place(x=150, y=300)

    choices = {1: "Rock", 2: "Scissors", 3: "Paper"}
    comp = choices[random.randint(1, 3)]

    if player == comp:
        results = "It's a tie."
    elif (player == "Rock" and comp == "Scissors") or \
         (player == "Paper" and comp == "Rock") or \
         (player == "Scissors" and comp == "Paper"):
        results =  "Player wins."
    elif (player == "Rock" and comp == "Paper") or \
         (player == "Paper" and comp == "Scissors") or \
         (player == "Scissors" and comp == "Rock"):
        results =  "AI wins."
    else:
        results =  "Invalid entry found"
    

    pitchFrame.insert(END, f"AI's choice: {comp}")
    pitchFrame.insert(END, f"Player's choice: {player}")
    pitchtext.insert(END, (results))

def StartGame():
    btnView.config(text="End")
    global groundFrame
    groundFrame = Listbox(root, width=80, height=20)
    groundFrame.place(x=20, y=130)
    btnRock = Button(groundFrame, text='Rock', bd=0, activeforeground='black',
                        bg='white', fg="black", font=('Arial', 15, 'bold'), command=lambda: gameLogic("Rock"))
    btnRock.place(x=10, y=10)
    btnPaper = Button(groundFrame, text='Paper', bd=0, activeforeground='black',
                        bg='white', fg="black", font=('Arial', 15, 'bold'), command=lambda: gameLogic("Paper"))
    btnPaper.place(x=10, y=110)
    btnScissors = Button(groundFrame, text='Scissors', bd=0, activeforeground='black',
                        bg='white', fg="black", font=('Arial', 15, 'bold'), command=lambda: gameLogic("Scissors"))
    btnScissors.place(x=10, y=220)



heading = Label(root, font=('Arial', 25, 'bold'), text="ROCK PAPER SCISSORS")
heading.place(x=230, y=40)

btnView = Button(root, text='Start', bd=0, activeforeground='black',
                    bg='white', fg="black", font=('Arial', 15, 'bold'), command=StartGame)
btnView.place(x=10, y=40)

logic = "Rock beats Scissors: Rock crushes Scissors.\
    Scissors beat Paper: Scissors cut Paper.\
        Paper beats Rock: Paper covers Rock."
subHeading = Label(root, text=logic)
subHeading.place(x=50, y=90)

root.mainloop()
