# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 08:31:25 2019
@author: DELL
"""

"""
------------------------------------------------------------------------
- Viết chương trình thực hiện yêu cầu sau:
    - Nhập: Từ tập tin văn bản Cau7A.inp 3 số nguyên A,B,C 
            có giá trị năng trong đoạn [-10^3, 10^3].
    - Xử lý: Giải phương trình Ax^2 + Bx+c = 0 trong trương hợp nghiệm thực, 
            kết quả làm tròn đến 1 chữ số thập phân.
    - Xuất: Ra tập tin văn bản Cau7A.out thong báo và các giá trị nghiệm nếu có.
    VD: Nếu A=1, B=2,C=1 thì thông báo 'Phương trình có nghiệm kép x1=x2' 
        và giá trị của nghiệm là -1.0
- Mục đích:
    + Viết 1 chương trình Python
    + Sử dụng câu lệnh if
    + Tổ chức chương trình một cách hợp lý
    + viết nhập xuất file
    + Viết và gọi thư viện
    + Viết và gọi hàm
------------------------------------------------------------------------
"""

from math import sqrt
from thuvien_gptb2 import nhap, delta

out_file = open('Cau7A.OUT','w') # mở để đọc nội dung với 'w'

# Hàm giải phương trình
def gpt(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                out_file.write("Phuong trinh VSN!") #ghi nội dung vào file
            else:
                out_file.write("Phuong trinh VN!") #ghi nội dung vào file
        else:
            if c == 0:
                out_file.write("Phuong trinh co 1 nghiem x = 0")
            else:
                out_file.write("Phuong trinh co 1 nghiem: x= %.1f" %(-b/a))            
    else:
        d = delta(a, b, c)
        if d < 0:
            out_file.write("Phuong trinh VN")
        elif d == 0:
            out_file.write("Phuong trinh co nghiem kep: x1 = x2 = %.1f" %(-b / (2 * a)))
        else:
            d = sqrt(d)
            x1 = (-b + d) / (2 * a)
            x2 = (-b - d) / (2 * a)
            out_file.write("Phuong trinh co 2 nghiem phan biet:\nx1 = %.1f \nx2 = %.1f" %(x1, x2))

# Hàm tương đương với hàm main trong C/C++
def main():
    a, b, c = nhap()
    gpt(a, b, c)
    out_file.close() #đóng file đóng file output
    print ("done")

# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()

