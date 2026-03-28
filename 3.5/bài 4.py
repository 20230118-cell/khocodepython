# Bài 4: Kiểm tra chia hết cho 2, 3

n = int(input("Nhập số nguyên dương: "))

if n <= 0:
    print("Vui lòng nhập số nguyên dương!")
else:
    if n % 2 == 0 and n % 3 == 0:
        print("Số chia hết cho cả 2 và 3")
    elif n % 2 == 0:
        print("Số chia hết cho 2")
    elif n % 3 == 0:
        print("Số chia hết cho 3")
    else:
        print("Số không chia hết cho 2 và 3")