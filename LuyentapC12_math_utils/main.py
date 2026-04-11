from math_utils import *

# ===== PHÂN SỐ =====
tu, mau = cong(1, 2, 3, 4)
print("Cộng phân số:", hien_thi(tu, mau))

tu, mau = tru(3, 4, 1, 2)
print("Trừ phân số:", hien_thi(tu, mau))

tu, mau = nhan(2, 3, 4, 5)
print("Nhân phân số:", hien_thi(tu, mau))

tu, mau = chia(2, 3, 4, 5)
print("Chia phân số:", hien_thi(tu, mau))


# ===== HÌNH HỌC =====
print("\nChu vi hình tròn:", chu_vi_hinh_tron(5))
print("Diện tích hình tròn:", dien_tich_hinh_tron(5))

print("\nChu vi HCN:", chu_vi_hcn(4, 6))
print("Diện tích HCN:", dien_tich_hcn(4, 6))