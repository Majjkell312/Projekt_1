n = int(input("Enter the number where you want to stop the program: "))
x = int(input("Enter the number whose divisors you want to know: "))
for i in range (n+1):
    if i%x==0:
        print(i)