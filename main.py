from tictactoe import printBoard
from fatorial import fatorial


theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

printBoard(theBoard)

theBoard[0,0] = 'x'

printBoard(theBoard)

print(fatorial(5))


