# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 08:52:23 2019

@author: DELL
"""

"""
Viết chương trình thực hiện các yêu cầu sau:
    - Nhập: từ tập tin văn bản Cau6A.inp 3 số nguyên dương A,B,C 
            có giá trị nằm trong đoạn [-10^3, 10^3].
    - Xử lý: kiểm tra điều kiện 3 cạnh của 1 tam giác của A,B,C. Nếu :
        Đúng: Tính diện tích của tam giác, kết quả làm tròn đến hai chữ số thập phân.
        Ngược lại: tìm giá trị nhỏ nhất MIN của 3 số A,B,C.
    - Xuất ra tập tin văn bản Cau6A.out giá trị của S hoặc MIN.
    VD: Nếu A =3, B=5, C=4 thì S = 6.00.
"""

import math

in_file = open('Cau6A.INP','r') #với 'r' mở để đọc nội dung
out_file = open('Cau6A.OUT','w') # mở để đọc nội dung với 'w'

def nhap():
    a,b,c = [float(i) for i in next(in_file).split()]
    return a,b,c

# Hàm Xử lý tam giác
def tamgiac(a,b,c):
    if (a+b)>c and (a+c)>b and (b+c)>a:
        p = (a+b+c)/2
        s = math.sqrt(p*(p-a)*(p-b)*(p-c))
        out_file.write("%.2f"%(s)) #ghi nội dung vào file
    else:
        min = a
        if min > b:
            min = b
        if min > c:
            min = c
        out_file.write("%.2f"%(min)) #ghi nội dung vào file

# Hàm tương đương với hàm main trong C/C++
def main():
   a,b,c = nhap()
   tamgiac(a,b,c)
   in_file.close() #đóng file input 
   out_file.close() #đóng file đóng file output
   print ("done")
    
# Gọi thực hiện hàm main
if __name__ == "__main__":
    main()
