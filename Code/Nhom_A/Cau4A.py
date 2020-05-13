# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 08:31:25 2019
@author: DELL
"""
"""
------------------------------------------------------------------------
Viết chương trình thực hiện các yêu cầu sau:
    - Nhập: Từ tập tin văn bản Cau4A.inp số nguyên dương N, N<= 10^6.
    - Xử lý: Tính kết quả biểu thưc đan dấu với S với:
        S = N^2 - (N-1)^2 + (N-2)^2-...1.
    - Xuất: ra tập tin văn bản Cau4A.out giá trị của S
    Vd: Nếu N = 5 thì S = 5^2 - 4^2 + 3^2 - 2^2 + 1^2 = 15
------------------------------------------------------------------------
"""

in_file = open('Cau4A.INP','r') #với 'r' mở để đọc nội dung
out_file = open('Cau4A.OUT','w') # mở để đọc nội dung với 'w'

#hàm Nhập
def nhap():
    indata = in_file.read() #đọc dữ liệu từ file
    n = int(indata)
    return n

# hàm xử lý bài toán
def xuly(n):
    s = 0
    dau = -1
    for i in range(1,n+1):
        dau = -dau
        s = s + i*dau**2
    out_file.write('%d'%(s)) #ghi nội dung vào file
 
# Hàm tương đương với hàm main trong C/C++
def main():
    n=nhap()
    xuly(n)
    in_file.close() #đóng file input 
    out_file.close() #đóng file đóng file output
    print ("done")
    
# gọi thực hiên hàm main
if __name__=="__main__":
    main()    