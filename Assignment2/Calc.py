import math


print(' 1.(a+b) \n 2.(a-b) \n 3.(a*b) \n 4.(a/b) \n 5.(a^b) \n 6.cos(a) \n 7.sin(a) \n 8.tan(a) \n 9.cot(a) \n 10.log(a) \n')
print('Choose the operation you want : ')
C = int(input())

if C<=5 and C>=1 :
    a=int(input("Enter a : "))
    b=int(input("Enter b : "))
    if C==1 :
        print (a ,'+', b ,'='  , (a+b))
    if C==2 :
        print (a ,'-', b ,'='  , (a-b))
    if C==3 :
        print (a ,'*', b ,'='  , (a*b))
    if C==4 :
        print (a ,'/', b ,'='  , (a/b))
    if C==5 :
        print (a ,'^', b ,'='  , (a**b))
elif C>=6 and C<=10  :  
    a=int(input("Enter a : "))
    if C==6:
        print('cos(',a,')','=',math.cos(math.radians(a)))
    if C==7:
        print('sin(',a,')','=',math.sin(math.radians(a)))
    if C==8:
        print('tan(',a,')','=',math.tan(math.radians(a)))
    if C==9:
        print('cot(',a,')','=',(1 / math.tan(math.radians(a))))
    if C==10:
        print('log(',a,')','=',math.log(a))

