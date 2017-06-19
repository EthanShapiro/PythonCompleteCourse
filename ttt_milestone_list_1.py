board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']
         ]

playerTurn = 1
play = True
playerPieces = ['x', 'o']


def showBoard():
    print("   1 2 3\n"
          "1 |{0}|{1}|{2}|\n"
          "2 |{3}|{4}|{5}|\n"
          "3 |{6}|{7}|{8}|".format(*[item for sublist in board for item in sublist])
          )


def placePiece(piece, xPos, yPos):
    if board[yPos][xPos] == ' ':
        board[yPos][xPos] = piece
        return True
    return False


def getNumOnBoard(posType):
    while True:
        try:
            pos = int(input("Enter an {0} location:".format(posType)))
        except ValueError:
            print("Please enter an integer")
            continue
        if pos <= 0:
            print("Please enter an number above 0")
            continue
        else:
            return pos-1


def checkForWin():
    threeInARow = lambda x, y, z: True if x == y == z and x != ' ' else False

    win = False

    for i in range(len(board)):
        win = threeInARow(*board[i][::])
        if win:
            return win

    for i in range(len(board)):
        win = threeInARow(*[x[i] for x in board])
        if win:
            return win

    win = threeInARow(*[board[i][i] for i in range(len(board))])
    if win:
        return win
    win = threeInARow(*[board[i][i] for i in range(len(board)-1, 0-1, -1)])
    if win:
        return win

    return win


def changePlayerIcons():
    player = 1
    while True:
        try:
            a = input("Player {0} enter your game piece: ".format(player))
        except ValueError:
            print("Sorry I didn't understand that")
            continue
        if len(a) > 1 or len(a) <= 0:
            print("Sorry, your icon needs to be one character long")
            continue
        elif a == playerPieces[0]:
            print("Sorry, you have to have different player pieces")
            continue
        elif player < len(playerPieces):
            playerPieces[player-1] = a
            player += 1
        else:
            playerPieces[player-1] = a
            break


def playAgain():
    while True:
        try:
            play = input("Play again? (y/n)")
        except ValueError:
            print("Sorry I didn't understand that")
            continue
        if len(play) > 1 or len(play) <= 0:
            print("Sorry, your icon needs to be one character long")
            continue
        elif play.lower() != 'y' and play.lower() != 'n':
            print("Please enter y or n")
        elif play.lower() == 'n':
            return False
        else:
            return True

changePlayerIcons()
checkForWin()

while play:
    showBoard()
    xPos = getNumOnBoard('x')
    yPos = getNumOnBoard('y')
    placePiece(playerPieces[playerTurn-1], xPos, yPos)
    if checkForWin():
        play = playAgain()
