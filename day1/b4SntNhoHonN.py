# in ra các số nguyên tố nhỏ hơn
n = int(input("n = "))

for i in range(1, n + 1):
    dem = 0
    for j in range(2, i):
        if (i % j == 0):
            dem += 1 
    if dem == 0: 
        print(i, end=" ")