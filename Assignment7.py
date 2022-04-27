class ComplexNumber :
    def __init__(self,a,b):
        self.a = a
        self.b = b 
    def sum (a,b):
        return ComplexNumber(  (a.a+b.a) , (a.b+b.b)  ) 
    def mul (a,b):
        return ComplexNumber(  ( (a.a*b.a)-(a.b*b.b) ) , ( (a.a*b.b)+(a.b*b.a) )   )
    def sub (a,b):
        return ComplexNumber(  (a.a-b.a) , (a.b-b.b)  )
    def Print(self):
        print(self.a ,"+", self.b ,end='')
        print("i")

a = ComplexNumber(int(input("Input first number's real part : ")),int(input("Input first number's image part :")))
b = ComplexNumber(int(input("Input second number's real part : ")),int(input("Input second number's image part :")))

while True : 
    print("Choose from options below : ")
    print("1- add ")
    print("2- sub ")
    print("3- multiply ")
    print("4- Exit")
    c=int(input())
    
    if c == 1 :
        a.sum(b).Print()
    if c == 2 :
        a.sub(b).Print()
    if c == 3 :
        a.mul(b).Print()
    if c == 4 :
        exit()
