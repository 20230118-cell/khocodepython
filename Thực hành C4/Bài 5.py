import os
from collections import Counter

# =========================
# 1. Khai báo tên file
# =========================
file_name = "demo_file2.txt"

# =========================
# 2. Tạo file nếu chưa có
# =========================
if not os.path.exists(file_name):
    with open(file_name, "w", encoding="utf-8") as f:
        f.write("Dem so luong tu xuat hien abc abc abc 12 12 it it eaut")
    print("✅ Đã tạo file demo_file2.txt")

# =========================
# 3. Đọc nội dung file
# =========================
with open(file_name, "r", encoding="utf-8") as f:
    text = f.read()

# =========================
# 4. Tách từ
# =========================
words = text.split()

# =========================
# 5. Đếm số lần xuất hiện
# =========================
count = Counter(words)

# =========================
# 6. Hiển thị kết quả
# =========================
print("\n📄 Nội dung file:")
print(text)

print("\n📊 Số lần xuất hiện của từng từ:")
for word, num in count.items():
    print(f"{word}: {num}")