import random


def display_board(board):
    print('{} | {} | {}'.format(board[7],board[8],board[9]))
    print('----------')
    print('{} | {} | {}'.format(board[4],board[5],board[6]))
    print('----------')
    print('{} | {} | {}'.format(board[1],board[2],board[3]))

test_board = ['#','X','O','X','O','X','O','X','O','X']


def clear_output():
    print('\n'*100)

def player_input():
    marker = input("Please pick a marker 'X' or 'O'").upper()
    while marker != 'X' or 'O':
        if  marker == 'X':
            player1 ='X'
            player2 ='O' 
            return(player1,player2)   
        else:
            player1 ='O'
            player2 ='X' 
            return(player1,player2)
        
   
def place_marker(board, marker, position):
    board[position] = marker

def win_check(board,mark):

    return((board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or 
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[1] == mark and board[5] == mark and board[9] == mark))
      


def choose_first():
    randomPlayer = random.randint(0,1)
    if randomPlayer > 0.5:
        return 'player1'
    else:
        return 'player2'

print(choose_first())
    
def space_check(board, position):
    return board[position] != 'X' and 'O' 


def full_board_check(board):
    return len(set(board)) == 3

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay():
    replay = input('Do you want to play ? Enter Y or N').upper()[0]
    while replay != 'Y' or 'N':
        if replay == 'Y':
            return True
        else: 
            return False




print('Welcome to Tic Tac Toe!')

while  True: 

    game_on =  replay()
    player1,player2 = player_input()
    print(f'The {choose_first()} will start the Game!')
    board = ['#','1','2','3','4','5','6','7','8','9']
    starter = choose_first()
    position = 0
    display_board(board)
    if game_on:   
        while game_on:
            if  starter == player1:
                position = player_choice(board)
                print(space_check(board,position))
                place_marker(board, player1, position)
                display_board(board)
                if win_check(board,player1):
                    clear_output()
                    print('Player 2 has won the Game!')               
                    replay()
                elif full_board_check(board):
                    clear_output()
                    replay()
                starter = player2
            else: 
                position = player_choice(board)
                place_marker(board, player2, position)
                display_board(board)
                if win_check(board,player2):
                    clear_output()
                    print('Player 2 has won the Game!')               
                    replay()
                elif full_board_check(board):
                    clear_output()
                    replay()
                starter = player1
    else: 
        print('THANKS for playing TIC TAC TOE')
        break

        
        
        # Player2's turn.
            
            #pass

    #if not replay():
        #break

        