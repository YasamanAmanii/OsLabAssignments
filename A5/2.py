n = int(input("Enter n : "))
m = int(input("Enter m : "))

for i in range(0,n) :
    for j in range (0,m) :
        if (j+i)%2==0 :
            print("🟩" , end="")
        else : 
            print("🟨" , end="")
    print()