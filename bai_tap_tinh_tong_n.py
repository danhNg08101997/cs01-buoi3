# Viết chương trình cho phép nhập vào số n. tính tổng số n đó

# Input
so_n = int(input("Nhập số n: "))
# Output
tong_so_n = 0
# Process
so_lan = 1
while so_lan <= so_n:
    tong_so_n = tong_so_n + so_lan
    so_lan = so_lan + 1

    print("Tổng số n: ", tong_so_n)