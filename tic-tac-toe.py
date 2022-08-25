from board import check_win, draw_board, check_turn
import os

spots = { 1 : "1", 2 : "2", 3 : "3", 4 : "4", 
5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9"
}

playing = True
turn = 0
prev_turn = -1

while playing:
    # Reset the screen 
    os.system('cls' if os.name == 'nt' else 'clear')
    draw_board(spots)

    # If an invalid turn occured, let the player know
    if prev_turn == turn:
        print("Invalid spote selected, please pick another.")

    prev_turn = turn
    print("Player" + str((turn % 2) + 1) + "'s turn: Pick your spot or press q to quit")

    # Get input from player
    choice = input()
    if choice == "q":
        playing = False

    # Check if input is within the 1-9 range
    elif str.isdigit(choice) and int(choice) in spots:
        # Check if spot is already taken
        if not spots[int(choice)] in {'X', 'O'}:

            # Valid input, update the board
            turn += 1
            spots[int(choice)] = check_turn(turn)
    
    # Check if someone has won
    if check_win(spots):
        playing, complete = False, True
    if turn > 8: 
        playing = False

# print the results and draw the board one last time
os.system('cls' if os.name == 'nt' else 'clear')
draw_board(spots)

# If there's a winner, congratulate
if complete:
    if check_turn(turn) == 'X':
        print("Player 1 wins!")
    else:
        print("Player 2 wins!")
else:
    print("No winner")

print("Thanks for playing")
