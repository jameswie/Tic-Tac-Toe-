#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Function to print out Board

from IPython.display import clear_output

def display_board(board):
    
    clear_output()
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-'+' - '+'- ')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-'+' - '+'- ')
    print(board[1]+'|'+board[2]+'|'+board[3])


# In[2]:


# Write funtion that takes a player input and assigns their marker to X or O

def player_input():
    marker = ''
    
    # Keep asking player 1 to choose X or O
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1, choose X or O: ').upper()
        
    if marker == 'X':
        
        return ('X','O')
    else:
        return ('O','X')
    


# In[3]:


# Write a function that takes in player 1 input (X or O) and assigns it to a position

def place_marker(board, marker, position):
    

    board[position] = marker
    


# In[4]:


# Write a funciton that takes in a board and a marker and checks for a win

def win_check(board,mark):
    

# Check if all rows share the same mark
# Check if all columns share same mark
# Check if both diagnoal share same mark

    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[7] == mark and board[4] == mark and board[1] == mark:
        return True
    elif board[8] == mark and board[5] == mark and board[2] == mark:
        return True
    elif board[9] == mark and board[6] == mark and board[3] == mark:
        return True
    elif board[7] == mark and board[5] == mark and board[3] == mark:
        return True
    elif board[9] == mark and board[5] == mark and board[1] == mark:
        return True
    else:
        pass



# In[5]:


# Write a function that Write a function that uses the random module to randomly decide 
# which player goes first. You may want to lookup random.randint() Return a string of which player went first

def choose_first():
    import random
    
    k = random.randint(1,10)
    
    if k % 2 == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# In[6]:


# Write a function that returns a boolean determining whether a space on the board is empty or filled

def space_check(board,position):
    return board[position] == ' ' 


# In[7]:


# Write a function that determined if the whole board is full, True if full, false if otherwise

def full_board_check(board):
    
    for i in range(1,10):
        
        if space_check(board,i):
            return False
        
        
    return True
        
    
    
        
    


# In[8]:


# Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to 
# check if it's a free position. If it is, then return the position for later use.

def player_choice(board):
    
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Choose a position (1-9): '))
        
    return position


# In[9]:


# Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.

def replay():
    
    answer = input('Do you want to play again? (Y or N): ')
    
    if answer == 'Y':
        return True
    if answer == 'N':
        return False
    
    


# In[ ]:


print('Welcome to Tic Tac Toe!')

while True:
    # Reset the board
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player1_marker, position)

            if win_check(theBoard, player1_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.
            
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player2_marker, position)

            if win_check(theBoard, player2_marker):
                display_board(theBoard)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break


# In[ ]:




