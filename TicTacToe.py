### GLOBAL VARIABLES ###

#Turn Counter
counter = 0

#TicTacToe Board Variables
row1 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
row2 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
row3 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
row4 = ['-','-','-','-','-','-','-','-','-','-','-']
row5 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
row6 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
row7 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
row8 = ['-','-','-','-','-','-','-','-','-','-','-']
row9 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
row10 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
row11 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
board = [row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11]

#Board Places
placements = ['1','2','3','4','5','6','7','8','9']

#Static lists
symbol_lst = ['X','O']
yesno = ['Y','N']

#Player Symbols
p1sym = []
p2sym = []

#Start Game Function
def game_start(player1=True):
    #Welcome
    print('Welcome to Tic Tac Toe!\n')
    #Player 1 select symbol and check if X or O input
    while player1 == True:
        p1choice = input('Player 1: Would you like to be X or O? \n').upper()
        if p1choice not in symbol_lst:
            print('Sorry, not a valid symbol!')
        #if p1choice is X, adds 'X' to p1sym and 'O' to p2sym
        elif p1choice in symbol_lst and p1choice == 'X':
            p1sym.append('X')
            p2sym.append('O')
            player1 = False
            game_ready()
            break
        #Vice-Versa of above code
        elif p1choice in symbol_lst and p1choice == 'O':
            p1sym.append('O')
            p2sym.append('X')
            player1 = False
            game_ready()
        else:
            pass

#Ready Check
def game_ready(readycheck=False):
    #After selection has been made, ask if ready to begin.
    while readycheck == False:
        p1ready = input('\nAre you ready to begin? Y or N \n').upper()
        if p1ready not in yesno:
            print('Invalid choice. Please re-enter valid option.')
        elif p1ready in yesno and p1ready == 'N':
            break
        else:
            readycheck = True
            print('\nGood luck players! \nMATCH START!\n')
            reset_board()
            p1_turn()
            break

#Take turns function
def turn_helper(symbol:str) -> None:
    global counter
    move = True
    while move:
        inpt = input(f'\nPlayer 1 -- Where would you like to place your {symbol}? (1-9)\n')
        match inpt:
            case '1':
                row10[1] = symbol
                move = False
            case '2':
                row10[5] = symbol
                move = False
            case '3':
                row10[9] = symbol
                move = False
            case '4':
                row6[1] = symbol
                move = False
            case '5':
                row6[5] = symbol
                move = False
            case '6':
                row6[9] = symbol
                move = False
            case '7':
                row2[1] = symbol
                move = False
            case '8':
                row2[5] = symbol
                move = False
            case '9':
                row2[9] = symbol
                move = False
            case _:
                print('Invalid placement. Please re-enter valid option.')
    current_board()
    alter_placement(inpt, symbol)
    counter += 1


def alter_placement(player_choice:str, symbol:str) -> None:
    #cast user input to deal with indexes-- NOTE subtract 1 because index pos starts at 0
    player_choice_int = int(player_choice) - 1
    #call global placements list
    global placements
    #change index number of new int player choice and replaces corresponding value in list with player symbol
    placements[player_choice_int] = symbol

def p1_turn():
    if check_win(board,['X','O']) == True:
        return None
    turn_helper(p1sym[0])
    p2_turn()

def p2_turn():
    if check_win(board,['X','O']) == True:
        return None
    turn_helper(p2sym[0])
    p1_turn()

#Function to reset board
def reset_board() -> list:
    #Call all global variables since we're resetting and reassigning
    global row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11,board,placements,counter
    counter = 0
    placements = ['1','2','3','4','5','6','7','8','9']
    row1 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
    row2 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
    row3 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
    row4 = ['-','-','-','-','-','-','-','-','-','-','-']
    row5 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
    row6 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
    row7 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
    row8 = ['-','-','-','-','-','-','-','-','-','-','-']
    row9 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
    row10 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
    row11 = [' ',' ',' ','|',' ',' ',' ','|',' ',' ',' ']
    board = [row1,row2,row3,row4,row5,row6,row7,row8,row9,row10,row11]
    for i in board:
        print(''.join(i))
    
def current_board() -> list:
    print('\n' * 10)
    for i in board:
        print(''.join(i))

def check_win(board,symbol_lst):
    win = False
    #Player 1 Win Conditions
    if row10[1] == p1sym[0] and row10[5] == p1sym[0] and row10[9] == p1sym[0]:
        print('Congrats! Player 1 Wins!')
        win = True
        play_again()
        return win
    elif row6[1] == p1sym[0] and row6[5] == p1sym[0] and row6[9] == p1sym[0]:
        print('Congrats! Player 1 Wins!')
        win = True
        play_again()
        return win
    elif row2[1] == p1sym[0] and row2[5] == p1sym[0] and row2[9] == p1sym[0]:
        print('Congrats! Player 1 Wins!')
        win = True
        play_again()
        return win
    elif row10[1] == p1sym[0] and row6[1] == p1sym[0] and row2[1] == p1sym[0]:
        print('Congrats! Player 1 Wins!')
        win = True
        play_again()
        return win
    elif row10[5] == p1sym[0] and row6[5] == p1sym[0] and row2[5] == p1sym[0]:
        print('Congrats! Player 1 Wins!')
        win = True
        play_again()
        return win
    elif row10[9] == p1sym[0] and row6[9] == p1sym[0] and row2[9] == p1sym[0]:
        print('Congrats! Player 1 Wins!')
        win = True
        play_again()
        return win
    elif row10[1] == p1sym[0] and row6[5] == p1sym[0] and row2[9] == p1sym[0]:
        print('Congrats! Player 1 Wins!')
        win = True
        play_again()
        return win
    elif row10[9] == p1sym[0] and row6[5] == p1sym[0] and row2[1] == p1sym[0]:
        print('Congrats! Player 1 Wins!')
        win = True
        play_again()
        return win
    else:
        win = False
    
    #Player 2 Win Conditions
    if row10[1] == p2sym[0] and row10[5] == p2sym[0] and row10[9] == p2sym[0]:
        print('Congrats! Player 2 Wins!')
        win = True
        play_again()
        return win
    elif row6[1] == p2sym[0] and row6[5] == p2sym[0] and row6[9] == p2sym[0]:
        print('Congrats! Player 2 Wins!')
        win = True
        play_again()
        return win
    elif row2[1] == p2sym[0] and row2[5] == p2sym[0] and row2[9] == p2sym[0]:
        print('Congrats! Player 2 Wins!')
        win = True
        play_again()
        return win
    elif row10[1] == p2sym[0] and row6[1] == p2sym[0] and row2[1] == p2sym[0]:
        print('Congrats! Player 2 Wins!')
        win = True
        play_again()
        return win
    elif row10[5] == p2sym[0] and row6[5] == p2sym[0] and row2[5] == p2sym[0]:
        print('Congrats! Player 2 Wins!')
        win = True
        play_again()
        return win
    elif row10[9] == p2sym[0] and row6[9] == p2sym[0] and row2[9] == p2sym[0]:
        print('Congrats! Player 2 Wins!')
        win = True
        play_again()
        return win
    elif row10[1] == p2sym[0] and row6[5] == p2sym[0] and row2[9] == p2sym[0]:
        print('Congrats! Player 2 Wins!')
        win = True
        play_again()
        return win
    elif row10[9] == p2sym[0] and row6[5] == p2sym[0] and row2[1] == p2sym[0]:
        print('Congrats! Player 2 Wins!')
        win = True
        play_again()
        return win
    else:
        win = False
        
    #Tie Conditions
    if counter == 9:
        print('TIE GAME!')
        play_again()
        win = True
        return win

#Function to play again
def play_again():
    playagain = True
    while playagain == True:
        replay = input('Would you like to play again? Y or N? \n').upper()
        if replay not in yesno:
            print('Sorry, invalid choice. Please re-enter option.')
        elif replay in yesno and replay == 'N':
            print('\nGame Over!\nSee you next time!')
            break
        elif replay in yesno and replay == 'Y':
            game_start()
            break
        else:
            pass

if __name__ == '__main__':
    game_start()