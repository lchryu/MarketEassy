'''
b1:
nhập vào 1 số nguyên n
đếm tất cả các ước của số nguyên đấy
6: 1 2 3 6
'''
while(1):
    n = int(input("n = "))

    count = 2
    # duyệt các ước của n (1 <= x <= n)
    for x in range(2, n):
        # nếu n chia hết cho x
        if n % x == 0:
            count += 1
    print("Số ước của", n ,"là:", count)

