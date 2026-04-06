# bảng mã
code_dict = {
    'a': '!',
    'b': '@',
    'c': '#',
    'd': '$'
}

# tạo bảng giải mã
decode_dict = {v: k for k, v in code_dict.items()}

text = input("Nhập chuỗi: ")

# mã hóa
encoded = ""
for ch in text:
    encoded += code_dict.get(ch, ch)

print("Chuỗi mã hóa:", encoded)

# giải mã
decoded = ""
for ch in encoded:
    decoded += decode_dict.get(ch, ch)

print("Chuỗi giải mã:", decoded)