from tictactoe import printBoard


theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

printBoard(theBoard)

theBoard[0,0] = 'x'

printBoard(theBoard)


