# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 21:37:11 2019

@author: HadesSecurity
"""

"""
------------------------------------------------------------------------
Viết chương trình thực hiện các yêu càu sau:
    - Nhập: Từ tập tin văn bản Cau3A.inp số nguyên dương N, N <=10^6.
    - Xử lý: Tính S là tổng các chữ số của N.
    - Xuất: ra tập tin Cau3A.out giá trị của S.
    VD: Nếu N = 423157698 thì S = 4+2+3+1+5+7+6+9+8=45.
------------------------------------------------------------------------
"""
in_file = open('Cau3A.INP','r') #với 'r' mở để đọc nội dung
out_file = open('Cau3A.OUT','w') # mở để đọc nội dung với 'w'

#hàm Nhập
def nhap():
    indata = in_file.read() #đọc dữ liệu từ file
    n = int(indata)
    return n

# hàm xử lý bài toán
def xuly(n):
    s = 0
    while (n!=0) :
        s+= n%10
        n = n//10
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