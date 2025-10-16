# this is the library that generates random numbers or choices
import random

import time

def computers_move():
    # create our list of valid options that the computer will pick from
    options_list = ["rock", "paper","scissors"]
    
    # pick randomly from options_list 
    computer_choice = random.choice(options_list)
    
    # wait one second to make everyone think we're doing super advanced AI!
    time.sleep(1)
    
    # return the random choice from above
    return computer_choice

computers_move()

def rock_paper_scissors_round(player1,player2):
    
    result = "\U0001F937" # this initializes it first
    
    player1 = player1.lower() ## makes it lowercase
    player2 = player2.lower()
    
    if player1 == "rock":
        if player2 == "rock":
            result = "draw"
        elif player2 == "paper":
            result = "Player 2 wins"
        elif player2 == "scissors":
            result = "Player 1 wins"
    elif player1 == "paper":
        if player2 == "rock":
            result = "Player 1 wins"
        elif player2 == "paper":
            result = "draw"
        elif player2 == "scissors":
            result = "Player 2 wins"
    elif player1 == "scissors":
        if player2 == "rock":
            result = "Player 2 wins"
        elif player2 == "paper":
            result = "Player 1 wins"
        elif player2 == "scissors":
            result = "draw"
                
    print(player1, " vs ", player2, " :", result)
    return result 

def rock_paper_scissors_game(player1, player2):
    if type(player1) == str and type(player2) == str:
        rock_paper_scissors_round(player1, player2) ## call the function
    else:
        grimacing_face_emoji_ucode = "\U0001F62C"
        if type(player1) != str:
            print("Player 1 input is not a string.")
        
        if type(player2) != str:
            print("Player 2 input is not a string.")
        
        return "Both inputs should be strings " + grimacing_face_emoji_ucode # insert the grimacing face emoji here

from codexutils import with_buttons

# with_buttons lets us run a function in response to clicking a button
# corresponding to these choices (rock/paper/scissors)
print("Click on a button to make your move. The computer will randomly choose something next.")
@with_buttons(["rock", "paper", "scissors"])
def rps_game(my_move_player1):
    print("Player 1, You chose: ", str(my_move_player1))
    player2_computer = computers_move()
    print("Player 2, Computer chooses: ", str(player2_computer))
    rock_paper_scissors_game(my_move_player1, player2_computer)
