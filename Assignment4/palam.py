import random

print('choose from options below : ')
print(' 1-Roo \n 2-Posht \n')
User = int(input())
Comp1 = random.randint(1, 2)
Comp2 = random.randint(1, 2)
while Comp1 == User == Comp2:
    Comp1 = random.randint(1, 2)
    Comp2 = random.randint(1, 2)
  
if Comp1==1 :
    print("Comouter1 chooses Roo")
if Comp1==2 :
    print("Comouter1 chooses posht")
if Comp2==1 :
    print("Comouter2 chooses Roo")
if Comp2==2 :
    print("Comouter2 chooses posht")
 
if Comp1 == Comp2 and Comp1 != User :
    print ('User Wins!!')
if Comp1 == User and Comp2 != User :
    print ('Computer2 Wins!!')
if Comp2 == User and Comp1 != User :
    print ('Computer1 Wins!!')