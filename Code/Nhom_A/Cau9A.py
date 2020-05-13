# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 19:12:11 2019

@author: DELL
"""

# -*- coding: utf-8 -*-
"""
Viết chương trình thực hiện các yêu càu sau:
    - Nhập: Từ tập tin văn bản Cau9A.inp 2 số nguyên dương M, N, M,N<=10^6.
    - Xử lý: Tìm tất cả các số nguyên tố nằm trong đoạn [M,N].
    - Xuất: ra ra tập tin văn bản Cau9A.out danh sách các số nguyên tố,
            mỗi số cách nhau bởi 1 khoảng trắng.
    VD: nếu M = 1, n=10 thì các số nguyên tố tìm được là 2,3,5,7.
"""

import math

in_file = open('Cau9A.INP','r') #với 'r' mở để đọc nội dung
out_file = open('Cau9A.OUT','w') # mở để đọc nội dung với 'w'

# hàm nhập m,n
def nhap():
    m,n = [int(i) for i in next(in_file).split()]
    return m,n

# Hàm kiểm tra 1 số nguyên dương x có phải là số nguyên tố?
def ktnt(x):
    k = int(math.sqrt(x)) + 1
    for i in range(2, k):
        if x % i == 0:
            return False
    return True

# Hàm tìm các số nguyên tố trong đoạn [m,n]
def dsnt(m, n):
    ds = []
    if m < 2:
        m = 2
    for i in range(m, n + 1):
        if ktnt(i):
            ds.append(i)
    return ds

# Hàm tương đương với hàm main trong C/C++
def main():
    # Nhập và kiểm tra dữ liệu nhập
    while True:
        m, n = nhap()
        if m < n:
            break
        
    # Đếm và liệt kê danh sách các số nguyên tố thuộc đoạn [m, n]
    ds = dsnt(m, n)
    out_file.write("%s" %ds)
    in_file.close() #đóng file input 
    out_file.close() #đóng file đóng file output
    print ("done")


# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()


