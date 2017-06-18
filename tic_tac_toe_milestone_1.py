board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}

play = True
placeSuccess = True
while(play):
    if(placeSuccess == True):



def printBoard():
    print("\n"*10)
    print("|{0}|{1}|{2}|    |{9}|{10}|{11}|\n"
          "|{3}|{4}|{5}|    |{12}|{13}|{14}|\n"
          "|{6}|{7}|{8}|    |{15}|{16}|{17}|".format(*board.values(), *board.keys()))

def placePiece(piece, pos):
    if board[str(pos)] == ' ':
        board[str(pos)] = piece
    else:
        print()

def getPos():
    pass

printBoard()
placePiece('c', 4)
printBoard()

