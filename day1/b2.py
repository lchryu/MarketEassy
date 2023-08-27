# in ra các ước của n
n = int(input("n= "))
luutru = 0
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")