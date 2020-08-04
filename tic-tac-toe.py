import os
from bs4 import BeautifulSoup
board=[' ' for x in range(10)]


def insertBoard(letter, pos):
    board[pos]=letter

def spaceIsFree(pos):
    return board[pos]==' '
def isWinner(bo, le):
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
    (bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
    (bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
    (bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
    (bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
    (bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
    (bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
    (bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal
def playerMove():
    run=True
    while run:
        move=input(' enter place 1-9 : ')
        try:
            move=int(move)
            if move>0 and move < 10:
                if spaceIsFree(move):
                    run=False
                    insertBoard('X',move)
                else:
                    print('this place occuped !')
            else:
                print('type number with the range 1-9')
        except:
            print('enter valid numb! ')
def selectRandom(li):
    import random
    ln= len(li)
    r=random.randrange(0, ln)
    return li[r]
def compMove():
    possibleMoves=[x for x, letter in enumerate(board) if letter== ' ' and x !=0]
    move=0
    for let in  ['O', 'X']:
        for i in possibleMoves:
            boardcopy=board[:]
            boardcopy[i]=let
            if isWinner(boardcopy, let):
                move=i
                return move
    cornersOpen=[]
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
    if len(cornersOpen)>0:
        move=selectRandom(cornersOpen)
        return move
    if 5 in possibleMoves:
        move=5
        return move
    edgesOpen=[]
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
    if len(edgesOpen)>0:
        move=selectRandom(edgesOpen)
    return move

def isBoardFull(board):
    if board.count(' ')>1:
        return False
    else:
        return True
def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
def main():
    print('welcome')
    printBoard(board)
    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('O\'s won this time ...')
            break

        if not(isWinner(board,'X')):
            move=compMove()
            if move==0:
                print('Game is a Tie')
            else:
                insertBoard('O',move)
                print('comp has place an o in place:',move)
                printBoard(board)
        else:
            print('X\'s won , good job ')
            break



main()
