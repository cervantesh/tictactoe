from IPython.display import clear_output

'''
Outputs a aboard representation on the console.
'''

def display_board(board):
    clear_output()
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
'''
Prompts player 1 for the selection of his marker.
'''

def player_input():
    selection = ' '
    while selection != 'X' and  selection != 'O':
        selection = input('Select your marker. Options are X or O: ').upper()

    if selection == 'X':
        return ('X','O')
    else:
        return ('O','X')


'''
Sets a marker in a board position.
'''

def place_marker(board, marker, position):
    board[position] = marker

'''
Checks if a player has won. 
'''

def win_check(board,mark):
    win = (
        (board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[7] == mark and board[8] == mark and board[9] == mark) or

        (board[1] == mark and board[4] == mark and board[7] == mark) or
        (board[2] == mark and board[5] == mark and board[8] == mark) or
        (board[3] == mark and board[6] == mark and board[9] == mark) or

        (board[1] == mark and board[5] == mark and board[9] == mark) or
        (board[3] == mark and board[5] == mark and board[7] == mark)
    )
    return win



'''
Randomly selects whos is the first and second player. 
'''
import random
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


'''
Check if a space in a position is free
'''

def space_check(board, position):
    return board[position] == ' '

'''
Verify if the boar is full of marks 
'''

def full_board_check(board):
    for index in range(1,10):
        if space_check(board,index):
            return False
    return True


'''
Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function 
from step 6 to check if its a free position. If it is, then return the position for later use.
'''

def player_choice(board):
    # Using strings because of raw_input
    position = ' '
    options = ['1','2','3','4','5','6','7','8','9']
    while position not in options or not space_check(board, int(position)):
        position = input('Choose your next position: (1-9) ')
    return int(position)

'''
Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.
'''
def replay():
    return input("Play again. Enter Yes or No: ").lower().startswith('y')

'''
Step 10: Here comes the hard part! Use while loops and the functions you've made to run the game!
'''

print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    gameBoard = [' '] * 10
    marker1, marker2 = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    game_on = True

    while game_on:
        display_board(gameBoard)
        position = player_choice(gameBoard)
        if turn == 'Player 1':
            place_marker(gameBoard, marker1, position)

            if win_check(gameBoard, marker1):
                display_board(gameBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(gameBoard):
                    display_board(gameBoard)
                    print('Tie!')
                    break
                else:
                    turn = 'Player 2'

        else:
            place_marker(gameBoard, marker2, position)

            if win_check(gameBoard, marker2):
                display_board(gameBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(gameBoard):
                    display_board(gameBoard)
                    print('Tie!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break