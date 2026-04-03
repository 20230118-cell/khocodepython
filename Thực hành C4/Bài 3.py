# Tạo file
with open("demo_file1.txt", "w", encoding="utf-8") as f:
    f.write("Thuc\nhanh\nvoi\nfile\nIO")

# a) In 1 dòng
with open("demo_file1.txt", "r", encoding="utf-8") as f:
    print("👉 In 1 dòng:")
    print(f.read().replace("\n", " "))

# b) In từng dòng
with open("demo_file1.txt", "r", encoding="utf-8") as f:
    print("👉 In từng dòng:")
    for line in f:
        print(line.strip())