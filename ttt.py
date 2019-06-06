from colorama import Fore, Style
import sys

#globals
state = {} 
board = {
    'a1': ' ',
    'a2': ' ',
    'a3': ' ',
    'b1': ' ',
    'b2': ' ',
    'b3': ' ',
    'c1': ' ',
    'c2': ' ',
    'c3': ' '
}
state['going'] = True
state['player'] = 1
state['banner'] = '''------------------------
Let\'s play Py-Pac-Poe!
------------------------'''

#functions

def turn():
    while state['going']:
        m = None
        move = input(f'Player {state["player"]}, make your move!:  ').lower()
        if move in list(board.keys()) and board[move] == ' ':
            if state['player'] == 1:
                m = Fore.RED + 'X' + Fore.WHITE
            else:
                m = Fore.GREEN + 'O' + Fore.WHITE
            board[move] = m
            if state['player'] == 1:
                state['player'] = 2
            else:
                state['player'] = 1
        else: 
            print('That\'s not a valid move!\n')
            turn()

        render(board)
        win = winner()
        if win:
            print(Fore.GREEN + 'Winner, congrats player ' + str(state["player"]) + Fore.WHITE)
            break        

def render(board):
    print(f'''
            A   B   C
            
        1)  {board["a1"]} | {board["b1"]} | {board["c1"]} 
            -----------
        2)  {board["a2"]} | {board["b2"]} | {board["c2"]} 
            -----------
        3)  {board["a3"]} | {board["b3"]} | {board["c3"]} 

        ''' )
    # print(state['template'])

def winner():
    if ' ' in board.values():
        if board['a1'] == board['b1'] == board['c1'] and board['a1'] !=' ':
            return True
        if board['a2'] == board['b2'] == board['c2'] and board['a2'] !=' ':
            return True
        if board['a3'] == board['b3'] == board['c3'] and board['a3'] !=' ':
            return True
        if board['a1'] == board['a2'] == board['a3'] and board['a1'] !=' ':
            return True
        if board['b1'] == board['b2'] == board['b3'] and board['b1'] !=' ':
            return True
        if board['c1'] == board['c2'] == board['c3'] and board['c1'] !=' ':
            return True
        if board['a1'] == board['b2'] == board['c3'] and board['a1'] !=' ':
            return True
        if board['a3'] == board['b2'] == board['c1'] and board['c1'] !=' ':
            return True
    else:
            print('TIE GAME!')
            sys.exit()
                                                        
render(board)
turn()