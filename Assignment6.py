class Kasr :
    def __init__(self,s,m):
        self.s = s
        self.m = m 
    
    def sum (a,b):
        a.s *= b.m
        b.s *= a.m
        a.m *=b.m
        b.m = a.m
        a.s += b.s

    def sub (a,b):
        a.s *= b.m
        b.s *= a.m
        a.m *=b.m
        b.m = a.m
        a.s -= b.s
    
    def mul (a,b):
        a.m *= b.m
        a.s *= b.s
        
    def div (a,b):
        a.m *= b.s
        a.s *= b.m
    
    def Show(self):
        for i in range(self.s,1,-1):
            if self.s%i==0 and self.m%i==0 :
                self.s //=i
                self.m //=i
        print(self.s,'\\',self.m)


a = Kasr(int(input("Soorat kasr a : ")),int(input("Makhraj kasr a = ")))
b = Kasr(int(input("Soorat kasr b : ")),int(input("Makhraj kasr b = ")))

print("Choose from options below : ")
print("1- a*b ")
print("2- a/b ")
print("3- a+b ")
print("4- a-b ")
c=int(input())
if c == 1 :
    a.mul(b)
    a.Show()
if c == 2 :
    a.div(b)
    a.Show()
if c == 3 :
    a.sum(b)
    a.Show()
if c == 4 :
    a.sub(b)
    a.Show()
