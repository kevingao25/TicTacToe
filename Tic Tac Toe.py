# Tic Tac Toe game with python
# 2020-08-15, first python project through tutorial
# https://www.youtube.com/watch?v=5s_lGC2sxwQ

board = [' ' for i in range(10)]


def insertLetter(letter, position):
    board[position] = letter


def spaceIsFree(position):
    return board[position] == ' '


def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')


def isWinner(board, letter):
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            (board[1] == letter and board[5] == letter and board[9] == letter) or
            (board[3] == letter and board[5] == letter and board[7] == letter) or
            (board[1] == letter and board[4] == letter and board[7] == letter) or
            (board[2] == letter and board[5] == letter and board[8] == letter) or
            (board[3] == letter and board[6] == letter and board[9] == letter))


def playerMove():
    run = True
    while run:
        move = input("Please select a position to place an \'X\', (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print("Sorry, This place is occupied")
            else:
                print("Please enter a valid number within the range")

        except:
            print("Please type a number")


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if x != 0 and letter == ' ']
    move = 0

    # Set a move if there is a winning move for computer or player
    for let in ('O', 'X'):
        for i in possibleMoves:  # Make a board copy for each possible moves and check if it wins
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    # Randomly set a move to take corner
    cornersOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    # Randomly set a move to take edge
    edgeOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgeOpen.append(i)

    if len(edgeOpen) > 0:
        move = selectRandom(edgeOpen)
    return move


def selectRandom(lst):
    import random
    ln = len(lst)
    r = random.randrange(0, ln)
    return lst[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print("Welcome to Tic Tac Toe")
    printBoard(board)

    while not (isBoardFull(board)):
        if not isWinner(board, 'O'):
            playerMove()
            printBoard(board)
        else:
            print("Sorry, O's won the game")
            break

        if not isWinner(board, 'X'):
            move = compMove()
            if move != 0:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move, ':')
                printBoard(board)
        else:
            print("Awesome, X\'s won the game")
            break

    if isBoardFull(board):
        print("Tie Game")


main()
while True:
    answer = input("Would you like to play another one?  (y/n)")
    if answer.lower() == 'y' or answer.lower() == 'yes':
        board = [' ' for i in range(10)]
        print("__________________________________")
        main()
    else:
        break
