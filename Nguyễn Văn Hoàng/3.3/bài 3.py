# Bài 3
import time

nam_sinh = int(input("Nhập năm sinh: "))

x = time.localtime()
year = x[0]   # hoặc x.tm_year

tuoi = year - nam_sinh

print(f"Năm sinh {nam_sinh}, vậy bạn {tuoi} tuổi.")