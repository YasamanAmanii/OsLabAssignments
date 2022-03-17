import random

N = int(input("Please eneter a number : "))
Counter = 1
Numbers = []
Numbers.append(random.randint( 0, 1000))

while Counter < N :    
    Duplicate = False
    Rnd = random.randint(0, 1000)
   
    for i in range(len(Numbers)) :
        if Numbers[i] == Rnd :
            Duplicate = True
   
    if Duplicate == False :
        Numbers.append(Rnd)
        Counter +=1

for i in range(N):
    print(Numbers[i] ,end=' ') 