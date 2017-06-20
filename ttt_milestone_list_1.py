board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']
         ]

playerTurn = 1
play = True
playerPieces = ['x', 'o']


def displayBoard():
    print("   1 2 3\n"
          "1 |{0}|{1}|{2}|\n"
          "2 |{3}|{4}|{5}|\n"
          "3 |{6}|{7}|{8}|".format(*[item for sublist in board for item in sublist])
          )


def clearConsole():
    print("\n"*20)


def resetBoard():
    for x in range(len(board)):
        for y in range(len(board[x])):
            board[x][y] = ' '


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
        elif pos > len(board):
            print("That is not a space on the board!")
            continue
        else:
            return pos-1


def checkForWin():
    threeInARow = lambda x, y, z: x if x == y == z and x != ' ' else ' '

    winner = ' '

    # Check Rows
    for i in range(len(board)):
        winner = threeInARow(*board[i][::])
        if winner != ' ':
            return winner

    # Check Columns
    for i in range(len(board)):
        winner = threeInARow(*[x[i] for x in board])
        if winner != ' ':
            return winner

    # Check Diagonal top right to bottom left
    winner = threeInARow(*[board[i][i] for i in range(len(board))])
    if winner != ' ':
        return winner

    # Check Diagonal top left to bottom right
    winner = threeInARow(*[board[i][len(board)-1-i] for i in range(len(board))])
    if winner != ' ':
        return winner

    # Check for Tie
    if not any(' ' in sublist for sublist in board):
        winner = 'tie'

    return winner


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

def endGameText(winner):
    if winner == 'tie':
        print("It's a tie!")
    else:
        print("The winner is {0}".format(winner))

changePlayerIcons()
checkForWin()

while play:
    displayBoard()
    xPos = getNumOnBoard('x')
    yPos = getNumOnBoard('y')

    while not placePiece(playerPieces[playerTurn-1], xPos, yPos):
        xPos = getNumOnBoard('x')
        yPos = getNumOnBoard('y')

    if checkForWin() == playerPieces[playerTurn-1] or checkForWin() == 'tie':
        endGameText(checkForWin())
        play = playAgain()
        if play:
            resetBoard()
    if playerTurn == 2:
        playerTurn = 1
    else:
        playerTurn += 1
