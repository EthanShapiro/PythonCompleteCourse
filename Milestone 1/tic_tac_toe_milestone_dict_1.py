board = {
    '1': ' ', '2': ' ', '3': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '7': ' ', '8': ' ', '9': ' '
}


def printBoard():
    print("|{0}|{1}|{2}|    |{9}|{10}|{11}|\n"
          "|{3}|{4}|{5}|    |{12}|{13}|{14}|\n"
          "|{6}|{7}|{8}|    |{15}|{16}|{17}|".format(*board.values(), *board.keys()))

def placePiece(piece, pos):
    if board[str(pos)] == ' ':
        board[str(pos)] = piece
        return True
    else:
        return False

def getPos():
    return input("Enter a position (1-9):\n")

def resetBoard():
    global board
    board = dict.fromkeys(board, ' ')

def getPiece():
    global playerTurn
    player1Piece = 'x'
    player2Piece = 'o'
    if playerTurn == 1:
        playerTurn = 2
        return player1Piece
    else:
        playerTurn = 1
        return player2Piece


def checkForWin():
    threeInARow = lambda x, y, z: x if x == y == z and x != ' ' else ' '
    vals = list(board.values())

    numPerRow = 3
    winner = ' '
    # Check rows
    for i in range(3, len(vals) + numPerRow, numPerRow):
        winner = threeInARow(*vals[i - numPerRow:i])
        if winner != ' ':
            return winner

    # Check Columns
    for i in range(0, numPerRow):
        print(*vals[i::3])
        winner = threeInARow(*vals[i::3])
        if winner != ' ':
            return winner

    # Check Diagonals
    winner = threeInARow(vals[0], vals[4], vals[8])
    if winner != ' ':
        return winner

    winner = threeInARow(vals[2], vals[4], vals[6])
    if winner != ' ':
        return winner
    return winner


def playAgain():
    return True if input("Play again? (y/n)").strip().lower() == 'y' else False


def printWinner(winnerPiece):
    print("{0} is the winner!".format(winnerPiece))

play = True
placeSuccess = True
playerTurn = 1

while play:
    winnerPiece = checkForWin()
    if winnerPiece != ' ':
        printWinner(winnerPiece)
    else:
        print("\n" * 20)  # To clear the screen of previous play

    if not placeSuccess:
        print("That space is occupied!")
    else:
        piece = getPiece()

    printBoard()
    placeSuccess = placePiece(piece, getPos())

