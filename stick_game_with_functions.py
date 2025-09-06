import time

print("Welcome players, who is player one, and who is player 2?")

def case_sensitive():   
    while True:
        player_1 = input("Player 1: ").strip()
        player_2 = input("Player 2: ").strip()

        if player_1 == player_2:
            print("Invalid input, Player 1 and Player 2 cannot have the same name. Please enter different names.")
        else:
            return player_1, player_2

player_1, player_2 = case_sensitive()

player_turn = 1

print("We are going to play a stick game, last one to pick the stick wins.\nBefore we thoroughly explain the game\n")

num_sticks = 0
while True:
    try:
        num_sticks = int(input("How many sticks do you want there to be (Between 1 - 100)? "))
        if num_sticks < 1 or num_sticks > 100:
            print("Invalid input, please pick a number between 1 - 100")
        else:
            print("In this game, there are going to be a total of", num_sticks, "sticks lined up in a row.\n")
            break  # Exit the loop when num_sticks is valid
    except ValueError:
        print("Invalid input, please enter an integer between 1 - 100")

scripts = [
    "Now, you're not going to see these sticks as you continue playing, but we will track each stick throughout the game to tell you how many are left.\n",
    "You will pick a number between 1-3, this will be the number of sticks you have taken out of the pile.\n",
    "Whoever takes the last stick from the pile wins the game.\n",
    "You ready? Let's go!"
]

for s in scripts:
    print(s)
    try:
        time.sleep(3)
    except KeyboardInterrupt:
        print("\nGame interrupted by the player.")
        exit()
    print("\n")

while num_sticks > 0:
    if player_turn == 1:
        current_player = player_1
    else:
        current_player = player_2

    try:
        sticks_taken = int(input(f"{current_player}, how many sticks are you going to take? (1-3): "))
    except ValueError:
        print("Invalid input, please enter an integer between 1 and 3.")
        continue

    if sticks_taken not in [1, 2, 3]:
        print("Invalid input, please pick the numbers 1, 2, or 3.")
    elif sticks_taken > num_sticks:
        print("Not enough sticks left to take that many.")
    else:
        num_sticks -= sticks_taken
        print(f"There are now {num_sticks} sticks left.")

        if num_sticks == 0:
            congratulatory_message = f"Congratulations {current_player}, you won the game!"
            print(congratulatory_message)
            break

        player_turn = 3 - player_turn   
        
        