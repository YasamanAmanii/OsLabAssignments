import time
import random

GameBoard = [['_','_','_'],
             ['_','_','_'],
             ['_','_','_']]
TimeStart = time.time()
def PrintBoard() :
    for i in range(3):
        for j in range(3):
            if GameBoard[i][j] == 'X':
                print("\033[1;31;40mX",end=' ')
            if GameBoard[i][j] == 'O':
                print("\033[1;34;40mO",end=' ')
            if GameBoard[i][j]=='_':
                print("\033[0;37;40m_",end=' ')
        print()
    print("\033[0;37;40m",end='')
                 
def CheckGame() :
    ExitBool = False
    for i in range(3):
        if GameBoard[i][0]=='X' and GameBoard[i][1]=='X' and GameBoard[i][2]=='X':
            print('Player 1 wins!')
            ExitBool = True
        if GameBoard[i][0]=='O' and GameBoard[i][1]=='O' and GameBoard[i][2]=='O':
            print('Player 2 wins!')
            ExitBool = True
        if GameBoard[0][i]=='X' and GameBoard[1][i]=='X' and GameBoard[2][i]=='X':
            print('Player 1 wins!')
            ExitBool = True
        if GameBoard[0][i]=='O' and GameBoard[1][i]=='O' and GameBoard[2][i]=='O':
            print('Player 2 wins!')
            ExitBool = True
    if GameBoard[0][0]=='X' and GameBoard[1][1]=='X' and GameBoard[2][2]=='X':
        print('Player 1 wins!')
        ExitBool = True
    if GameBoard[0][0]=='O' and GameBoard[1][1]=='O' and GameBoard[2][2]=='O':
        print('Player 2 wins!')
        ExitBool = True   
    if GameBoard[0][2]=='X' and GameBoard[1][1]=='X' and GameBoard[2][0]=='X':
        print('Player 1 wins!')
        ExitBool = True
    if GameBoard[0][2]=='O' and GameBoard[1][1]=='O' and GameBoard[2][0]=='O':
        print('Player 2 wins!')
        ExitBool = True  
    if ExitBool == True :
        TimeEnd=time.time()
        TimeElapsed = TimeEnd - TimeStart
        print("Time : " , int(TimeElapsed) , " Seconds")
        exit()

def TwoPlayers() :
    PrintBoard()
  
    Moves=0
    while True :  
        while True :
            print('Player 1')
            row = int(input("row : "))
            col = int(input("col : "))
            if 0<= row <=2 and 0<= col <=2 :
                if  GameBoard[row][col] == '_':
                    GameBoard[row][col] = 'X'
                    Moves+=1
                    break
                else :
                    print('this cell is not empty , try again!')
                break
            else :
                print('row and col must be betweem 0 and 2')
    
        PrintBoard()
        CheckGame()
        if Moves == 9 :
            print("Draw ! Nobody wins !")
            TimeEnd=time.time()
            TimeElapsed = TimeEnd - TimeStart
            print("Time : " , int(TimeElapsed) , " Seconds")
            exit()
        while True :
            print('Player 2')
            row = int(input("row : "))
            col = int(input("col : "))
            if 0<= row <=2 and 0<= col <=2 :
                if  GameBoard[row][col] == '_':
                    GameBoard[row][col] = 'O'
                    Moves+=1
                    break
                else :
                    print('this cell is not empty , try again!')
            else :
                print('row and col must be betweem 0 and 2')

        PrintBoard()
        CheckGame()

def SinglePlayer():
    PrintBoard()
    Moves=0
    while True :  
        while True :
            print('Player 1')
            row = int(input("row : "))
            col = int(input("col : "))
            if 0<= row <=2 and 0<= col <=2 :
                if  GameBoard[row][col] == '_':
                    GameBoard[row][col] = 'X'
                    Moves+=1
                    break
                else :
                    print('this cell is not empty , try again!')
                break
            else :
                print('row and col must be betweem 0 and 2')
    
        PrintBoard()
        CheckGame()
        if Moves == 9 :
            print("Draw ! Nobody wins !")
            TimeEnd=time.time()
            TimeElapsed = TimeEnd - TimeStart
            print("Time : " , int(TimeElapsed) , " Seconds")
            exit()
        while True :
            print('Computer :')
            row = random.randint(0,2)
            col = random.randint(0,2)
            if 0<= row <=2 and 0<= col <=2 :
                if  GameBoard[row][col] == '_':
                    GameBoard[row][col] = 'O'
                    Moves+=1
                    break

        PrintBoard()
        CheckGame()



print("Menu : ")
print("1- Play with computer ")
print("2- play with other player")
print("choose from the otions above (1/2) : " )
while True :
    UserChoice = int(input())
    if not 1 <= UserChoice <=2 :
        print("please enter a number 1 or 2 ! ")
    else :
        break
if UserChoice == 2 : 
    TwoPlayers()
elif UserChoice == 1  :
    SinglePlayer()