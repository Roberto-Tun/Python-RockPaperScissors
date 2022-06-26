import random #importing the random module

#function that prints a random action
def rpsselection():
    Actions = ["Rock", "Paper", "Scissors"] #list of actions
    AiSelection = random.choice(Actions) #using the random module to randomly select and an action from the list
    print(AiSelection) #printing the action selected

print("---------------------------------------------")
print("--------Welcome to Rock Paper Scissors-------") #welcome ui
print("---------------------------------------------")

Play = input("Would you like to play: Enter 'Y' or 'N' ") #asking the user if they would like to play

if Play.upper() == "Y":
    print("------------Moves-------------")
    print("1 | Rock")
    print("2 | Paper")
    print("3 | Scissors")
    UserAction = input("Enter your Move: ")

    

