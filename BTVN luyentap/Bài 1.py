# Bài 1
_tuple = ('a', 'b', 'd', 'e')

# chuyển sang list
temp = list(_tuple)

# thêm 'c' vào vị trí index 2
temp.insert(2, 'c')

# chuyển lại tuple
_new_tuple = tuple(temp)

print("Tuple mới:", _new_tuple)