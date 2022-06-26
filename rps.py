import random
from select import select #importing the random module

#function that prints a random action
def rpsselection():
    Actions = ["Rock", "Paper", "Scissors"] #list of actions
    AiSelection = random.choice(Actions) #using the random module to randomly select and an action from the list
    return AiSelection #when fucntion is called returns the random action selected

def insult():
    Insults = ["Your Ass", "Nice try kid", "Bozo", "ZZZZZ"]
    Insult_selected = random.choice(Insults)
    return Insult_selected

print("---------------------------------------------")
print("--------Welcome to Rock Paper Scissors-------") #welcome ui
print("---------------------------------------------")

Play = input("Would you like to play: Enter 'Y' or 'N' ") #asking the user if they would like to play

while Play.upper() == "Y":
    print("------------Moves-------------")
    print("1 | Rock")
    print("2 | Paper")
    print("3 | Scissors")
    UserAction = int(input("Enter your Move: "))

    Selection = rpsselection()

    if UserAction == 1:
        if Selection == "Paper":
            print("Your Move: \n", "Rock")
            print("AI's Move: \n", Selection)
            print(insult())
        elif Selection == "Scissors" or Selection == "Rock":
            print("Your Move: \n", "Rock")
            print("AI's Move: \n", Selection)
            print("GG")
    elif UserAction == 2:
        if Selection == "Scissors":
            print("Your Move: \n", "Paper")
            print("AI's Move: \n", Selection)
            print(insult())
        elif Selection == "Rock" or Selection == "Paper":
            print("Your Move: \n", "Paper")
            print("AI's Move: \n", Selection)
            print("GG")
    elif UserAction == 3:
        if Selection == "Rock":
            print("Your Move: \n", "Scissors")
            print("AI's Move: \n", Selection)
            print(insult())
        elif Selection == "Paper" or Selection == "Scissors":
            print("Your Move: \n", "Scissors")
            print("AI's Move: \n", Selection)
            print("GG")
    else:
        print("Invalid Input")

    Play = input("Would you like to continue playing: Enter 'Y' or 'N' ")

else:
    quit()
insult()

