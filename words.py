# https://inventwithpython.com/invent4thed/chapter8.html
# https://codereview.stackexchange.com/questions/136255/hangman-game-in-python
# https://www.google.com/search?q=how+to+make+a+hangman+game+in+python&oq=how+to+make+a+hangman+game&aqs=chrome.0.0i512j69i57j0i512l7j0i390.10203j0j7&sourceid=chrome&ie=UTF-8#kpvalbx=_6C1pYp2yDY3zgQais5VQ19



#import the random words
import random

"""def welcome():



  while True:
    welcome_msg = "Hello and welcome to Hangman World please select one of the following options by typing in the number beside your selection into the answer field" 
    print(welcome_msg)
    play = "1. Play Game"
    instructions = "2. Instructions"
    high_scores = "3. High Scores"
    quit ="4. Quit"
    start_choice = input("Enter your answer here 1,2,3,4: ")
    if start_choice == "1":
      print("You have choose play game")
    elif start_choice == "2":
      print("Hangman World is a word guessing game and as the name suggests the user will be asked to guess the name of the place in the world whoch the compuer has chosen.")
    elif start_choice == "3":
      print("display high scores")
    elif start_choice == "4":
      print("quitting game bye")
    else:
      print("you have not choose one of the selections please try again")

    

welcome()










words = ["europe", "america", "south america", "africa", 
"austraila", "asia", "antartica", "ireland", "england", "france", 
"germany", "spain", "portugal", "hungary", 
"belgium", "sweeden", "norway", "finland", 
"the netherlands", "italy", "bulgaria", "luxembourg", 
"morocco", "libya", "egypt", "sudan", 
"south africa", "chad", "mali", "nigeria", 
"kenya", "ethopia", "angola", "china", 
"india", "japan", "indonesia", "thailand", 
"the philippines", "south korea", "north korea", "sinapore", 
"texas", "florida", "california", "washington", "new york"]

#icons for the game
"""
# hangman_icons = [ """


#     -------
#     |     |
#     |     |
#     |
#     |
#     |
#     |
#   ----- """,
# """
#     -------
#     |     |
#     |     |
#     |     O
#     |
#     |
#     |
#   ----- """,
# """


#     -------
#     |     |
#     |     |
#     |     O
#     |     |
#     |
#     |
#   ----- """,
# """


#     -------
#     |     |
#     |     |
#     |     O
#     |     |/
#     |
#     |
#   -----  """,
# """
#     -------
#     |     |
#     |     |
#     |     O
#     |    \|/
#     |
#     |
#   ----- """,
# """

#     -------
#     |     |
#     |     |
#     |     O
#     |    \|/
#     |      \
#     |
#   -----   """,

# """
#     -------
#     |     |
#     |     |
#     |     O
#     |    \|/
#     |    / \
#     |
#   -----
  
#   """

# ]
# """


#print(hangman_icons)