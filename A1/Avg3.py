sum =0
for i in range(3):
    name = input("Enter course name : ")
    Score = float(input("Enter course Score : "))
    sum+=Score
Avg = sum/3 
print("Average : ", Avg)
