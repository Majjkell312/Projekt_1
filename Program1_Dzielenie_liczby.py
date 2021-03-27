n = int(input("Podaj na jakiej liczbie ma się zatrzymać twój program: "))
x = int(input("Podaj liczbe której dzielniki chcesz poznać: "))
for i in range (n+1):
    if i%x==0:
        print(i)