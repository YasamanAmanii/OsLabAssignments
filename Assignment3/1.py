n = int(input("how many numbers in your array ? "))
Sort =True

array = []
for i in range(n):
    array.append(int(input()))

for i in range(n):
    for j in range(i,n):
        if(array[i] > array[j]) :
            Sort=False           

if Sort == False :
     print("NOT SORTED!")
else :
    print ("SORTED!")