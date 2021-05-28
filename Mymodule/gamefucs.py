##TIC TAC TOE 

from IPython.display import clear_output
import random

def display_board(board):
    
    print(board[7], 'l', board[8] ,'l', board[9])
    print(board[4], 'l', board[5] ,'l', board[6])
    print(board[1], 'l', board[2] ,'l', board[3])

def player_input():
    marker = ''
    
    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Please choose a side, X or O').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position] = marker

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[7] == mark and board[4] == mark and board[1] == mark) or
    (board[8] == mark and board[5] == mark and board[2] == mark) or
    (board[9] == mark and board[6] == mark and board[3] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or
    (board[9] == mark and board[5] == mark and board[1] == mark))

def choose_first():
    if random.randint(0,1) ==0:
        return "player1"
    else:
        return "player2"

def space_check(board, position):
    return board[position] == ' '

def full_board_check(board):
    for pos in range(1,10):
        if space_check (board, pos):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input("Please enter your preferred position(1-9)"))

    return position

def replay(ans):
    answer = (input("Would you like to play again? Y/N")).upper()
    if answer == "N":
        ans = False
    else:
        ans = True
    return ans
