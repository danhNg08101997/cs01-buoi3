# Nhận biết bài toán có sử dụng vòng lặp hay không:
# Kiểm tra xem số lần xuất hiên, hoặc phép tính + - * / có thực hiện lại nhiều lần hay không => nếu có bài toán vòng lặp, không là if hoặc khối lệnh bình thường

# 4 yếu tố cấu thành vòng lặp
# 1/ Giá trị bắt đầu (thay đổi)
# 2/ Biểu thức lặp (Đúng thì sẽ lặp)
# 3/ Khối lệnh xử lý
# 4/ Khối lệnh thay đổi diều kiện lặp (điều kiện lặp)

# Lấy ví dụ: in ra chữ Hello techX 10 lần
so_lan = 1
while so_lan <= 10:
    print("Hello techX")
    so_lan = so_lan + 1
    