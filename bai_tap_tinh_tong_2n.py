# Viết chương trình cho phép người dùng nhập vào 1 số nguyên n, tính tổng từ 2 đến 2n
# S = 2 + 4 + 6 + 2n

# Input
so_n = int(input("Nhập số n: "))
# Output
tong_so_2n = 0
# Process
bien_lap = 2
while bien_lap <= 2*so_n:
    tong_so_2n += bien_lap
    bien_lap += 2

print("Tổng số n là: ", tong_so_2n)