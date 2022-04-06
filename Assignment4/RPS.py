import random

UserScore = 0 
CompScore = 0

for x in range(5):
    print('choose from options below : ')
    print(' 1-Rock \n 2-paper \n 3-scissors \n')
    User = int(input())
    Comp = random.randint(1, 3)

    while Comp == User:
        Comp = random.randint(1, 3)

    if Comp==1 :
        print("Comouter chooses Rock")
    if Comp==2 :
        print("Comouter chooses paper")
    if Comp==3 :
        print("Comouter chooses scissors")
 
    if User ==1 and Comp ==3 :
        UserScore +=1
        print ("You Won")
    if User == 1 and Comp ==2 :
        CompScore +=1
        print ("You Lost")
    if User == 2 and Comp ==1 :
        UserScore +=1
        print ("You Won")
    if User == 2 and Comp ==3 :
        CompScore +=1
        print ("You Lost")
    if User == 3 and Comp ==2 :
        UserScore +=1
        print ("You Won")
    if User == 3 and Comp ==1 :
        CompScore +=1
        print ("You Lost")
  
print('User Score : ', UserScore)   
print('Computer Score : ', CompScore)
if UserScore > CompScore :
    print ('User Wins')
else :
    print('Computer Wins')