# nhập vào 1 số tự nhiên và kiểm tra xem đó có phải số nguyên tố 
n = int(input("n = "))
cnt = 0
for i in range(1, n + 1):
    if (n % i == 0):
        cnt+=1
if (n == 2):
    print("YES")
else:
    print("NO")