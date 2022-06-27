import random #importing the random module

UsersScore = 0 #keep track of the user's score

AIScore = 0 #keep track of the AI's score

#function that prints a random action
def rpsselection():
    Actions = ["Rock", "Paper", "Scissors"] #list of actions
    AI_Selection = random.choice(Actions) #randomly selects an action form the list
    return AI_Selection #returns the random action selected

def insult():
    Insults = ["Your Ass", "Eat shit", "Bozo", "ZZZZZ"] #list of insults
    Insult_selected = random.choice(Insults) #randomly selects an insult from the list
    return Insult_selected #returns the random insult selected

print("---------------------------------------------")
print("--------Welcome to Rock Paper Scissors-------") #welcome ui
print("---------------------------------------------")

Play = input("Would you like to play: Enter 'Y' or 'N' ") #asking the user if they would like to play

while Play.upper() == "Y": #while loop to let the game continue
    print("------------Moves-------------")
    print("1 | Rock")
    print("2 | Paper") #different moves ui
    print("3 | Scissors")

    UserAction = int(input("Enter your Move: ")) #asking the user for their move

    AISelection = rpsselection() #setting the ai's action in a variable

    if UserAction == 1: #if checking the users move
        print("Your Move: \n", "Rock")
        print("AI's Move: \n", AISelection)
        if AISelection == "Paper": #if checking the AI's move
            print(insult()) #insult function is called
            AIScore += 1 #add one to the AI score
        else:
            print("Nice")
            if AISelection == "Scissors": #checks if the user won and adds 1 to the score board
                UsersScore += 1
    elif UserAction == 2:
        print("Your Move: \n", "Paper")
        print("AI's Move: \n", AISelection)
        if AISelection == "Scissors":
            print(insult()) #insult function is called
            AIScore += 1 #add one to the AI score
        else:
            print("Nice")
            if AISelection == "Rock": #checks if the user won and adds 1 to the score board
                UsersScore += 1
    elif UserAction == 3:
        print("Your Move: \n", "Scissors")
        print("AI's Move: \n", AISelection)
        if AISelection == "Rock":
            print(insult()) #insult function is called
            AIScore += 1 #add one to the AI score
        else:
            print("Nice")
            if AISelection == "Paper": #checks if the user won and adds 1 to the score board
                UsersScore += 1
    else:
        print("Invalid Input")

    Play = input("Would you like to continue playing: Enter 'Y' or 'N' ") #checking if the user would like to continue

else: #prints the scores and ends game
    print("Your Score: \n", UsersScore)
    print("AI's Score: \n", AIScore)
    if AIScore > UsersScore:
        print("Your Booty")
    elif UsersScore > AIScore:
        print("Good Game")
    else:
        print("Nice")
    exit() #exits the program

