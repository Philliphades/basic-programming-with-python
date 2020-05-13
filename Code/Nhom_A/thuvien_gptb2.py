# -*- coding: utf-8 -*-
"""
- Thư viện chứa 1 số hàm dùng để giải phương trình bậc 2
"""
in_file = open('Cau7A.INP','r') #với 'r' mở để đọc nội dung

# Hàm nhập hệ số a, b, c cho phương trình bậc 2
def nhap():
    a,b,c = [float(i) for i in next(in_file).split()]
    return a, b, c
    in_file.close() #đóng file input 
    
# Hàm tính delta
def delta(a, b, c):
    return b ** 2 - 4 * a * c

