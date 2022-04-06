n = int(input("Enter n: "))
for i in range(0,n):
    print(" " * (n - i), "*" * (2*i + 1))
    
for i in range(n - 2, -1, -1):
    print(" " * (n - i), "*" * (2*i + 1))